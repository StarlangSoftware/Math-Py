from __future__ import annotations
from typing import Tuple, List, Union


class Tensor:
    """
    A class representing a multidimensional tensor that supports basic operations and broadcasting.
    """
    __data: list[float]
    __shape: Tuple[int, ...]
    __strides: Tuple[int, ...]

    def __init__(self, data: Union[List, List[List], List[List[List]]], shape: Tuple[int, ...] = None):
        """
        Initializes the tensor with given data and shape.

        :param data: Nested lists representing the tensor data.
        :param shape: The shape of the tensor. If None, the shape is inferred from the data.
        """
        if shape is None:
            shape = self.__infer_shape(data)
        flattened_data = self.__flatten(data)
        total_elements = len(flattened_data)
        if self.__compute_num_elements(shape) != total_elements:
            raise ValueError("Shape does not match the number of elements in data.")
        self.__shape = shape
        self.__strides = self.__compute_strides(shape)
        self.__data = flattened_data

    def getData(self) -> List[float]:
        return self.__data

    def getShape(self) -> Tuple[int, ...]:
        return self.__shape

    def __infer_shape(self, data: Union[List, List[List], List[List[List]]]) -> Tuple[int, ...]:
        """
        Infers the shape of the tensor from nested lists.

        :param data: Nested lists representing the tensor data.
        :return: Tuple representing the shape.
        """
        if isinstance(data, list):
            if len(data) == 0:
                return (0,)
            return (len(data), *self.__infer_shape(data[0]))
        return ()

    def __flatten(self, data: Union[List, List[List], List[List[List]]]) -> List[float]:
        """
        Flattens nested lists into a single list.

        :param data: Nested lists representing the tensor data.
        :return: Flattened list of tensor elements.
        """
        if isinstance(data, list):
            return [item for sublist in data for item in self.__flatten(sublist)]
        return [data]

    def __compute_strides(self, shape: Tuple[int, ...]) -> Tuple[int, ...]:
        """
        Computes the strides for each dimension based on the shape.

        :param shape: Tuple representing the tensor shape.
        :return: Tuple representing the strides.
        """
        strides = []
        product = 1
        for dim in reversed(shape):
            strides.append(product)
            product *= dim
        return tuple(reversed(strides))

    def __compute_num_elements(self, shape: Tuple[int, ...]) -> int:
        """
        Computes the total number of elements in the tensor based on its shape.

        :param shape: Tuple representing the tensor shape.
        :return: Total number of elements.
        """
        product = 1
        for dim in shape:
            product *= dim
        return product

    def __validate_indices(self, indices: Tuple[int, ...]):
        """
        Validates that indices are within the valid range for each dimension.
        """
        if len(indices) != len(self.__shape):
            raise IndexError(f"Expected {len(self.__shape)} indices but got {len(indices)}.")

        for i, index in enumerate(indices):
            if not (0 <= index < self.__shape[i]):
                raise IndexError(f"Index {indices} is out of bounds for shape {self.__shape}.")

    def concat(self, tensor: Tensor, dimension: int) -> Tensor:
        """
        Concatenates two tensors into a one.
        :param tensor: 2nd tensor for concatenation.
        :param dimension: to concatenate.
        :return: Concatenated Tensor.
        """
        start_index = 1
        end_index1 = 1
        end_index2 = 1
        for i in range(len(self.__shape)):
            if i >= dimension:
                end_index1 *= self.__shape[i]
                end_index2 *= tensor.__shape[i]
            else:
                start_index *= self.__shape[i]
        new_shape = []
        for i in range(len(self.__shape)):
            if i == dimension:
                new_shape.append(self.__shape[i] + tensor.__shape[i])
            else:
                new_shape.append(self.__shape[i])
        new_list = []
        for i in range(start_index):
            for j in range(end_index1):
                new_list.append(self.__data[i * end_index1 + j])
            for j in range(end_index2):
                new_list.append(self.__data[i * end_index2 + j])
        return Tensor(new_list, tuple(new_shape))

    def get(self, dimensions: Tuple[int, ...]) -> Tensor:
        """
        Returns the subtensor taking the given dimensions.
        :param dimensions: Given dimensions
        :return: a subTensor
        """
        new_shape = self.__shape[len(dimensions):len(self.__shape)]
        i = 0
        start = 0
        end = len(self.__data)
        while i < len(dimensions):
            parts = (end - start) // self.__shape[i]
            start += parts * dimensions[i]
            end = start + parts
            i = i + 1
        return Tensor(self.__data[start:end], tuple(new_shape))

    def getValue(self, indices: Tuple[int, ...]) -> float:
        """
        Retrieves the value at the given indices.

        :param indices: Tuple of indices specifying the position.
        :return: Value at the specified position.
        """
        self.__validate_indices(indices)  # Ensure indices are valid
        flat_index = sum(i * stride for i, stride in zip(indices, self.__strides))
        return self.__data[flat_index]

    def setValue(self, indices: Tuple[int, ...], value: float):
        """
        Sets the value at the given indices.

        :param indices: Tuple of indices specifying the position.
        :param value: Value to set at the specified position.
        """
        self.__validate_indices(indices)  # Ensure indices are valid
        flat_index = sum(i * stride for i, stride in zip(indices, self.__strides))
        self.__data[flat_index] = value

    def reshape(self, new_shape: Tuple[int, ...]) -> Tensor:
        """
        Reshapes the tensor to the specified new shape.

        :param new_shape: Tuple representing the new shape.
        :return: New tensor with the specified shape.
        """
        if self.__compute_num_elements(new_shape) != self.__compute_num_elements(self.__shape):
            raise ValueError("Total number of elements must remain the same.")
        return Tensor(self.__data, new_shape)

    def transpose(self, axes: Tuple[int, ...] = None) -> Tensor:
        """
        Transposes the tensor according to the specified axes.

        :param axes: Tuple representing the order of axes. If None, reverses the axes.
        :return: New tensor with transposed axes.
        """
        if not axes:
            axes = tuple(range(len(self.__shape) - 1, -1, -1))
        if sorted(axes) != list(range(len(self.__shape))):
            raise ValueError("Invalid transpose axes.")
        new_shape = tuple(self.__shape[axis] for axis in axes)
        flattened_data = self.__transpose_flattened_data(axes, new_shape)
        return Tensor(flattened_data, new_shape)

    def __transpose_flattened_data(self, axes: Tuple[int, ...], new_shape: Tuple[int, ...]) -> List[float]:
        """
        Rearranges the flattened data for transposition.

        :param axes: Tuple representing the order of axes.
        :param new_shape: Tuple representing the new shape.
        :return: Flattened list of transposed data.
        """
        new_strides = self.__compute_strides(new_shape)
        flattened_data = []
        for i in range(self.__compute_num_elements(new_shape)):
            new_indices = self.__unflatten_index(i, new_strides)
            original_indices = [new_indices[axes.index(dim)] for dim in range(len(self.__shape))]
            flattened_data.append(self.getValue(tuple(original_indices)))
        return flattened_data

    def __unflatten_index(self, flat_index: int, strides: Tuple[int, ...]) -> List[int]:
        """
        Converts a flat index to multi-dimensional indices based on strides.

        :param flat_index: The flat index to convert.
        :param strides: Tuple representing the strides.
        :return: List of multi-dimensional indices.
        """
        indices = []
        for stride in strides:
            indices.append(flat_index // stride)
            flat_index %= stride
        return indices

    def __broadcast_shape(self, shape1: Tuple[int, ...], shape2: Tuple[int, ...]) -> Tuple[int, ...]:
        """
        Determines the broadcasted shape of two tensors.

        :param shape1: Tuple representing the first tensor shape.
        :param shape2: Tuple representing the second tensor shape.
        :return: Tuple representing the broadcasted shape.
        """
        reversed_shape1 = list(reversed(shape1))
        reversed_shape2 = list(reversed(shape2))
        result_shape = []

        for dim1, dim2 in zip(reversed_shape1, reversed_shape2):
            if dim1 == dim2:
                result_shape.append(dim1)
            elif dim1 == 1 or dim2 == 1:
                result_shape.append(max(dim1, dim2))
            else:
                raise ValueError(f"Shapes {shape1} and {shape2} are not broadcastable")

        result_shape.extend(reversed_shape1[len(reversed_shape2):])
        result_shape.extend(reversed_shape2[len(reversed_shape1):])
        return tuple(reversed(result_shape))

    def broadcast_to(self, target_shape: Tuple[int, ...]) -> Tensor:
        """
        Broadcasts the tensor to the specified target shape.

        :param target_shape: Tuple representing the target shape.
        :return: New tensor with the target shape.
        """
        expanded_shape = [1] * (len(target_shape) - len(self.__shape)) + list(self.__shape)
        if not all(dim1 == dim2 or dim1 == 1 for dim1, dim2 in zip(expanded_shape, target_shape)):
            raise ValueError(f"Cannot broadcast shape {self.__shape} to {target_shape}")
        new_data = []
        target_strides = self.__compute_strides(target_shape)
        for index in range(self.__compute_num_elements(target_shape)):
            indices = self.__unflatten_index(index, target_strides)
            original_indices = tuple(
                idx if size > 1 else 0 for idx, size in zip(indices, expanded_shape)
            )
            new_data.append(self.getValue(original_indices))
        return Tensor(new_data, target_shape)

    def add(self, other: Tensor) -> Tensor:
        """
        Adds two tensors element-wise with broadcasting.

        :param other: The other tensor to add.
        :return: New tensor with the result of the addition.
        """
        broadcast_shape = self.__broadcast_shape(self.__shape, other.__shape)
        tensor1 = self.broadcast_to(broadcast_shape)
        tensor2 = other.broadcast_to(broadcast_shape)
        result_data = [
            tensor1.__data[i] + tensor2.__data[i]
            for i in range(self.__compute_num_elements(broadcast_shape))
        ]
        return Tensor(result_data, broadcast_shape)

    def subtract(self, other: Tensor) -> Tensor:
        """
        Subtracts one tensor from another element-wise with broadcasting.

        :param other: The other tensor to subtract.
        :return: New tensor with the result of the subtraction.
        """
        broadcast_shape = self.__broadcast_shape(self.__shape, other.__shape)
        tensor1 = self.broadcast_to(broadcast_shape)
        tensor2 = other.broadcast_to(broadcast_shape)
        result_data = [
            tensor1.__data[i] - tensor2.__data[i]
            for i in range(self.__compute_num_elements(broadcast_shape))
        ]
        return Tensor(result_data, broadcast_shape)

    def hadamardProduct(self, other: Tensor) -> Tensor:
        """
        Multiplies two tensors element-wise with broadcasting.

        :param other: The other tensor to multiply.
        :return: New tensor with the result of the multiplication.
        """
        broadcast_shape = self.__broadcast_shape(self.__shape, other.__shape)
        tensor1 = self.broadcast_to(broadcast_shape)
        tensor2 = other.broadcast_to(broadcast_shape)
        result_data = [
            tensor1.__data[i] * tensor2.__data[i]
            for i in range(self.__compute_num_elements(broadcast_shape))
        ]
        return Tensor(result_data, broadcast_shape)

    def multiply(self, other: Tensor) -> Tensor:
        """
        Performs matrix multiplication (batched if necessary).

        For tensors of shape (..., M, K) and (..., K, N), returns (..., M, N).

        :param other: Tensor with shape compatible for matrix multiplication.
        :return: Tensor resulting from matrix multiplication.
        """
        if self.__shape[-1] != other.__shape[-2]:
            raise ValueError(f"Shapes {self.__shape} and {other.__shape} are not aligned for multiplication.")
        batch_shape = self.__shape[:-2]
        m, k1 = self.__shape[-2:]
        k2, n = other.__shape[-2:]
        if k1 != k2:
            raise ValueError("Inner dimensions must match for matrix multiplication.")
        # Broadcasting batch shape if necessary
        if batch_shape != other.__shape[:-2]:
            broadcast_shape = self.__broadcast_shape(self.__shape[:-2], other.__shape[:-2])
            self_broadcasted = self.broadcast_to(broadcast_shape + (m, k1))
            other_broadcasted = other.broadcast_to(broadcast_shape + (k2, n))
        else:
            broadcast_shape = batch_shape
            self_broadcasted = self
            other_broadcasted = other
        result_shape = broadcast_shape + (m, n)
        result_data = []
        for i in range(self.__compute_num_elements(result_shape)):
            indices = self.__unflatten_index(i, self.__compute_strides(result_shape))
            batch_idx = tuple(indices[:-2])
            row, col = indices[-2], indices[-1]
            sum_result = 0
            for k in range(k1):
                a_idx = batch_idx + (row, k)
                b_idx = batch_idx + (k, col)
                sum_result += self_broadcasted.getValue(a_idx) * other_broadcasted.getValue(b_idx)
            result_data.append(sum_result)
        return Tensor(result_data, result_shape)
    
    def partial(self, start_indices: Tuple[int, ...], end_indices: Tuple[int, ...]) -> Tensor:
        """
        Extracts a sub-tensor from the given start indices to the end indices.

        :param start_indices: Tuple specifying the start indices for each dimension.
        :param end_indices: Tuple specifying the end indices (exclusive) for each dimension.
        :return: A new Tensor containing the extracted sub-tensor.
        """
        if len(start_indices) != len(self.__shape) or len(end_indices) != len(self.__shape):
            raise ValueError("start_indices and end_indices must match the number of dimensions.")
        # Compute the new shape of the extracted sub-tensor
        new_shape = tuple(end - start for start, end in zip(start_indices, end_indices))
        # Extract data from the original tensor
        sub_data = []
        new_strides = self.__compute_strides(new_shape)
        for i in range(self.__compute_num_elements(new_shape)):
            sub_indices = self.__unflatten_index(i, new_strides)
            original_indices = tuple(start + offset for start, offset in zip(start_indices, sub_indices))
            sub_data.append(self.getValue(original_indices))
        return Tensor(sub_data, new_shape)

    def format_tensor(self, data: List[float], shape: Tuple[int, ...]) -> Union[float, List]:
        if len(shape) == 1:
            return data
        stride = self.__compute_num_elements(shape[1:])
        return [self.format_tensor(data[i * stride:(i + 1) * stride], shape[1:]) for i in range(shape[0])]

    def __repr__(self) -> str:
        """
        Returns a string representation of the tensor.

        :return: String representing the tensor.
        """
        formatted_data = self.format_tensor(self.__data, self.__shape)
        return f"Tensor(shape={self.__shape}, data={formatted_data})"
