# Math-Py
For Developers
============
You can also see either [Java](https://github.com/olcaytaner/Math) 
or [C++](https://github.com/olcaytaner/Math-CPP) repository.
## Requirements

* [Python 3.7 or higher](#python)
* [Git](#git)

### Python 

To check if you have a compatible version of Python installed, use the following command:

    python -V
    
You can find the latest version of Python [here](https://www.python.org/downloads/).

### Git

Install the [latest version of Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

## Download Code

In order to work on code, create a fork from GitHub page. 
Use Git for cloning the code to your local or below line for Ubuntu:

	git clone <your-fork-git-link>

A directory called Math will be created. Or you can use below link for exploring the code:

	git clone https://github.com/olcaytaner/Math-Py.git

## Open project with Pycharm IDE

Steps for opening the cloned project:

* Start IDE
* Select **File | Open** from main menu
* Choose `Math-PY` file
* Select open as project option
* Couple of seconds, dependencies will be downloaded. 


## Compile

**From IDE**

After being done with the downloading and Maven indexing, select **Build Project** option from **Build** menu. After compilation process, user can run DataStructure.

Detailed Description
============
+ [Vector](#vector)
+ [Matrix](#matrix)
+ [Distribution](#distribution)

## Vector

Bir vektör yaratmak için:

	Vector(self, values=None)

Vektörler eklemek için

	addVector(self, v: Vector)

Çıkarmak için

	subtract(self, v: Vector)
	difference(self, v: Vector) -> Vector

İç çarpım için

	dotProduct(self, v: Vector) -> float
	dotProductWithSelf(self) -> float

Bir vektörle cosinüs benzerliğini hesaplamak için

	double cosineSimilarity(Vector v)

Bir vektörle eleman eleman çarpmak için

	elementProduct(self, v: Vector) -> Vector

## Matrix

3'e 4'lük bir matris yaratmak için

	a = Matrix(3, 4)

Elemanları rasgele değerler alan bir matris yaratmak için

	Matrix(self, row, col, minValue=None, maxValue=None)

Örneğin, 

	a = Matrix(3, 4, 1, 5)
 
3'e 4'lük elemanları 1 ve 5 arasında değerler alan bir matris yaratır.

Matrisin i. satır, j. sütun elemanını getirmek için 

	getValue(self, rowNo: int, colNo: int) -> float

Örneğin,

	a.getValue(3, 4)

3. satır, 4. sütundaki değeri getirir.

Matrisin i. satır, j. sütunundaki elemanı değiştirmek için

	setValue(self, rowNo: int, colNo: int, value: float)

Örneğin,

	a.setValue(3, 4, 5)

3. satır, 4.sütundaki elemanın değerini 5 yapar.

Matrisleri toplamak için

	add(self, m: Matrix)

Çıkarmak için 

	subtract(self, m: Matrix)

Çarpmak için 

	multiply(self, m: Matrix) -> Matrix

Elaman eleman matrisleri çarpmak için

	elementProduct(self, m: Matrix) -> Matrix

Matrisin transpozunu almak için

	transpose(self) -> Matrix

Matrisin simetrik olup olmadığı belirlemek için

	isSymmetric(self) -> bool

Determinantını almak için

	determinant(self) -> float

Tersini almak için

	inverse(self)

Matrisin eigenvektör ve eigendeğerlerini bulmak için

	characteristics(self) -> list

Bu metodla bulunan eigenvektörler eigendeğerlerine göre büyükten küçüğe doğru 
sıralı olarak döndürülür.

## Distribution

Verilen bir değerin normal dağılımdaki olasılığını döndürmek için

	zNormal(z: float) -> float

Verilen bir olasılığın normal dağılımdaki değerini döndürmek için

	zInverse(p: float) -> float

Verilen bir değerin chi kare dağılımdaki olasılığını döndürmek için

	chiSquare(x: float, freedom: int) -> float

Verilen bir olasılığın chi kare dağılımdaki değerini döndürmek için

	chiSquareInverse(p: float, freedom: int) -> float

Verilen bir değerin F dağılımdaki olasılığını döndürmek için

	fDistribution(F: float, freedom1: int, freedom2: int) -> float

Verilen bir olasılığın F dağılımdaki değerini döndürmek için

	fDistributionInverse(p: float, freedom1: int, freedom2: int) -> float

Verilen bir değerin t dağılımdaki olasılığını döndürmek için

	tDistribution(T: float, freedom: int) -> float

Verilen bir olasılığın t dağılımdaki değerini döndürmek için

	tDistributionInverse(p: float, freedom: int) -> float
