from typing import Tuple, List, Union


class Tensor:
    """
    A class representing a multi-dimensional tensor that supports basic operations and broadcasting.
    """

    def __init__(self, data: Union[List, List[List], List[List[List]]], shape: Tuple[int, ...] = None):
        """
        Initializes the tensor with given data and shape.

        :param data: Nested lists representing the tensor data.
        :param shape: The shape of the tensor. If None, the shape is inferred from the data.
        """
        if shape is None:
            shape = self._infer_shape(data)

        flattened_data = self._flatten(data)
        total_elements = len(flattened_data)

        if self._compute_num_elements(shape) != total_elements:
            raise ValueError("Shape does not match the number of elements in data.")

        self.shape = shape
        self.strides = self._compute_strides(shape)
        self.data = flattened_data

    def _infer_shape(self, data: Union[List, List[List], List[List[List]]]) -> Tuple[int, ...]:
        """
        Infers the shape of the tensor from nested lists.

        :param data: Nested lists representing the tensor data.
        :return: Tuple representing the shape.
        """
        if isinstance(data, list):
            if len(data) == 0:
                return (0,)
            return (len(data), *self._infer_shape(data[0]))
        return ()

    def _flatten(self, data: Union[List, List[List], List[List[List]]]) -> List[float]:
        """
        Flattens nested lists into a single list.

        :param data: Nested lists representing the tensor data.
        :return: Flattened list of tensor elements.
        """
        if isinstance(data, list):
            return [item for sublist in data for item in self._flatten(sublist)]
        return [data]

    def _compute_strides(self, shape: Tuple[int, ...]) -> Tuple[int, ...]:
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

    def _compute_num_elements(self, shape: Tuple[int, ...]) -> int:
        """
        Computes the total number of elements in the tensor based on its shape.

        :param shape: Tuple representing the tensor shape.
        :return: Total number of elements.
        """
        product = 1
        for dim in shape:
            product *= dim
        return product

    def get(self, indices: Tuple[int, ...]) -> float:
        """
        Retrieves the value at the given indices.

        :param indices: Tuple of indices specifying the position.
        :return: Value at the specified position.
        """
        if len(indices) != len(self.shape):
            raise IndexError("Number of indices must match the tensor dimensions.")
        flat_index = sum(i * stride for i, stride in zip(indices, self.strides))
        return self.data[flat_index]

    def set(self, indices: Tuple[int, ...], value: float):
        """
        Sets the value at the given indices.

        :param indices: Tuple of indices specifying the position.
        :param value: Value to set at the specified position.
        """
        if len(indices) != len(self.shape):
            raise IndexError("Number of indices must match the tensor dimensions.")
        flat_index = sum(i * stride for i, stride in zip(indices, self.strides))
        self.data[flat_index] = value

    def reshape(self, new_shape: Tuple[int, ...]) -> "Tensor":
        """
        Reshapes the tensor to the specified new shape.

        :param new_shape: Tuple representing the new shape.
        :return: New tensor with the specified shape.
        """
        if self._compute_num_elements(new_shape) != self._compute_num_elements(self.shape):
            raise ValueError("Total number of elements must remain the same.")
        return Tensor(self.data, new_shape)

    def transpose(self, axes: Tuple[int, ...] = None) -> "Tensor":
        """
        Transposes the tensor according to the specified axes.

        :param axes: Tuple representing the order of axes. If None, reverses the axes.
        :return: New tensor with transposed axes.
        """
        if not axes:
            axes = tuple(range(len(self.shape) - 1, -1, -1))
        if sorted(axes) != list(range(len(self.shape))):
            raise ValueError("Invalid transpose axes.")

        new_shape = tuple(self.shape[axis] for axis in axes)
        flattened_data = self._transpose_flattened_data(axes, new_shape)
        return Tensor(flattened_data, new_shape)

    def _transpose_flattened_data(self, axes: Tuple[int, ...], new_shape: Tuple[int, ...]) -> List[float]:
        """
        Rearranges the flattened data for transposition.

        :param axes: Tuple representing the order of axes.
        :param new_shape: Tuple representing the new shape.
        :return: Flattened list of transposed data.
        """
        new_strides = self._compute_strides(new_shape)

        flattened_data = []
        for i in range(self._compute_num_elements(new_shape)):
            new_indices = self._unflatten_index(i, new_strides)
            original_indices = [new_indices[axes.index(dim)] for dim in range(len(self.shape))]
            flattened_data.append(self.get(tuple(original_indices)))

        return flattened_data

    def _unflatten_index(self, flat_index: int, strides: Tuple[int, ...]) -> List[int]:
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

    def _broadcast_shape(self, shape1: Tuple[int, ...], shape2: Tuple[int, ...]) -> Tuple[int, ...]:
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

    def broadcast_to(self, target_shape: Tuple[int, ...]) -> "Tensor":
        """
        Broadcasts the tensor to the specified target shape.

        :param target_shape: Tuple representing the target shape.
        :return: New tensor with the target shape.
        """
        expanded_shape = [1] * (len(target_shape) - len(self.shape)) + list(self.shape)
        if not all(dim1 == dim2 or dim1 == 1 for dim1, dim2 in zip(expanded_shape, target_shape)):
            raise ValueError(f"Cannot broadcast shape {self.shape} to {target_shape}")

        new_data = []
        for index in range(self._compute_num_elements(target_shape)):
            indices = self._unflatten_index(index, self._compute_strides(target_shape))
            original_indices = tuple(
                idx if size > 1 else 0 for idx, size in zip(indices, expanded_shape)
            )
            new_data.append(self.get(original_indices))

        return Tensor(new_data, target_shape)

    def __add__(self, other: "Tensor") -> "Tensor":
        """
        Adds two tensors element-wise with broadcasting.

        :param other: The other tensor to add.
        :return: New tensor with the result of the addition.
        """
        broadcast_shape = self._broadcast_shape(self.shape, other.shape)
        tensor1 = self.broadcast_to(broadcast_shape)
        tensor2 = other.broadcast_to(broadcast_shape)
        result_data = [
            tensor1.get(self._unflatten_index(i, tensor1.strides)) +
            tensor2.get(self._unflatten_index(i, tensor2.strides))
            for i in range(self._compute_num_elements(broadcast_shape))
        ]
        return Tensor(result_data, broadcast_shape)

    def __sub__(self, other: "Tensor") -> "Tensor":
        """
        Subtracts one tensor from another element-wise with broadcasting.

        :param other: The other tensor to subtract.
        :return: New tensor with the result of the subtraction.
        """
        broadcast_shape = self._broadcast_shape(self.shape, other.shape)
        tensor1 = self.broadcast_to(broadcast_shape)
        tensor2 = other.broadcast_to(broadcast_shape)
        result_data = [
            tensor1.get(self._unflatten_index(i, tensor1.strides)) -
            tensor2.get(self._unflatten_index(i, tensor2.strides))
            for i in range(self._compute_num_elements(broadcast_shape))
        ]
        return Tensor(result_data, broadcast_shape)

    def __mul__(self, other: "Tensor") -> "Tensor":
        """
        Multiplies two tensors element-wise with broadcasting.

        :param other: The other tensor to multiply.
        :return: New tensor with the result of the multiplication.
        """
        broadcast_shape = self._broadcast_shape(self.shape, other.shape)
        tensor1 = self.broadcast_to(broadcast_shape)
        tensor2 = other.broadcast_to(broadcast_shape)
        result_data = [
            tensor1.get(self._unflatten_index(i, tensor1.strides)) *
            tensor2.get(self._unflatten_index(i, tensor2.strides))
            for i in range(self._compute_num_elements(broadcast_shape))
        ]
        return Tensor(result_data, broadcast_shape)

    def dot(self, other: "Tensor") -> "Tensor":
        """
        Computes the dot product of two tensors.

        :param other: The other tensor to compute the dot product with.
        :return: New tensor with the result of the dot product.
        """
        if self.shape[-1] != other.shape[-2]:
            raise ValueError(f"Shapes {self.shape} and {other.shape} are not aligned for dot product.")

        result_shape = self.shape[:-1] + (other.shape[-1],)
        result_data = []

        for i in range(self._compute_num_elements(result_shape)):
            result_indices = self._unflatten_index(i, self._compute_strides(result_shape))
            dot_product = 0

            for k in range(self.shape[-1]):
                a_indices = tuple(result_indices[:-1]) + (k,)
                b_indices = (k,) + tuple(result_indices[-1:])
                dot_product += self.get(a_indices) * other.get(b_indices)

            result_data.append(dot_product)

        return Tensor(result_data, result_shape)

    def __repr__(self) -> str:
        """
        Returns a string representation of the tensor.

        :return: String representing the tensor.
        """
        def format_tensor(data: List[float], shape: Tuple[int, ...]) -> Union[float, List]:
            if len(shape) == 1:
                return data
            stride = self._compute_num_elements(shape[1:])
            return [format_tensor(data[i * stride:(i + 1) * stride], shape[1:]) for i in range(shape[0])]

        formatted_data = format_tensor(self.data, self.shape)
        return f"Tensor(shape={self.shape}, data={formatted_data})"
