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

	a = Vector(ArrayList<Double> values)

Vektörler eklemek için

	void add(Vector v)

Çıkarmak için

	void subtract(Vector v)
	Vector difference(Vector v)

İç çarpım için

	double dotProduct(Vector v)
	double dotProduct()

Bir vektörle cosinüs benzerliğini hesaplamak için

	double cosineSimilarity(Vector v)

Bir vektörle eleman eleman çarpmak için

	Vector elementProduct(Vector v)

## Matrix

3'e 4'lük bir matris yaratmak için

	a = Matrix(3, 4)

Elemanları rasgele değerler alan bir matris yaratmak için

	Matrix(int row, int col, double min, double max)

Örneğin, 

	a = Matrix(3, 4, 1, 5)
 
3'e 4'lük elemanları 1 ve 5 arasında değerler alan bir matris yaratır.

Birim matris yaratmak için

	Matrix(int size)

Örneğin,

	a = Matrix(4)

4'e 4'lük köşegeni 1, diğer elemanları 0 olan bir matris yaratır.

Matrisin i. satır, j. sütun elemanını getirmek için 

	double getValue(int rowNo, int colNo)

Örneğin,

	a.getValue(3, 4)

3. satır, 4. sütundaki değeri getirir.

Matrisin i. satır, j. sütunundaki elemanı değiştirmek için

	void setValue(int rowNo, int colNo, double value)

Örneğin,

	a.setValue(3, 4, 5)

3. satır, 4.sütundaki elemanın değerini 5 yapar.

Matrisleri toplamak için

	void add(Matrix m)

Çıkarmak için 

	void subtract(Matrix m)

Çarpmak için 

	Matrix multiply(Matrix m)

Elaman eleman matrisleri çarpmak için

	Matrix elementProduct(Matrix m)

Matrisin transpozunu almak için

	Matrix transpose()

Matrisin simetrik olup olmadığı belirlemek için

	boolean isSymmetric()

Determinantını almak için

	double determinant()

Tersini almak için

	void inverse()

Matrisin eigenvektör ve eigendeğerlerini bulmak için

	ArrayList<Eigenvector> characteristics()

Bu metodla bulunan eigenvektörler eigendeğerlerine göre büyükten küçüğe doğru 
sıralı olarak döndürülür.

## Distribution

Verilen bir değerin normal dağılımdaki olasılığını döndürmek için

	static double zNormal(double z)

Verilen bir olasılığın normal dağılımdaki değerini döndürmek için

	static double zInverse(double p)

Verilen bir değerin chi kare dağılımdaki olasılığını döndürmek için

	static double chiSquare(double x, int freedom)

Verilen bir olasılığın chi kare dağılımdaki değerini döndürmek için

	static double chiSquareInverse(double p, int freedom)

Verilen bir değerin F dağılımdaki olasılığını döndürmek için

	static double fDistribution(double F, int freedom1, int freedom2)

Verilen bir olasılığın F dağılımdaki değerini döndürmek için

	static double fDistributionInverse(double p, int freedom1, int freedom2)

Verilen bir değerin t dağılımdaki olasılığını döndürmek için

	static double tDistribution(double T, int freedom)

Verilen bir olasılığın t dağılımdaki değerini döndürmek için

	static double tDistributionInverse(double p, int freedom)
