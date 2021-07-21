#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-zoo
Version  : 1.8.9
Release  : 71
URL      : https://cran.r-project.org/src/contrib/zoo_1.8-9.tar.gz
Source0  : https://cran.r-project.org/src/contrib/zoo_1.8-9.tar.gz
Summary  : S3 Infrastructure for Regular and Irregular Time Series (Z's
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-zoo-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
observations. It is particularly aimed at irregular time series
             of numeric vectors/matrices and factors. zoo's key design goals
             are independence of a particular index/date/time class and
             consistency with ts and base R by providing methods to extend
             standard generics.

%package lib
Summary: lib components for the R-zoo package.
Group: Libraries

%description lib
lib components for the R-zoo package.


%prep
%setup -q -c -n zoo
cd %{_builddir}/zoo

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1615391869

%install
export SOURCE_DATE_EPOCH=1615391869
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library zoo
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library zoo
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library zoo
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/zoo/CITATION
/usr/lib64/R/library/zoo/DESCRIPTION
/usr/lib64/R/library/zoo/INDEX
/usr/lib64/R/library/zoo/Meta/Rd.rds
/usr/lib64/R/library/zoo/Meta/demo.rds
/usr/lib64/R/library/zoo/Meta/features.rds
/usr/lib64/R/library/zoo/Meta/hsearch.rds
/usr/lib64/R/library/zoo/Meta/links.rds
/usr/lib64/R/library/zoo/Meta/nsInfo.rds
/usr/lib64/R/library/zoo/Meta/package.rds
/usr/lib64/R/library/zoo/Meta/vignette.rds
/usr/lib64/R/library/zoo/NAMESPACE
/usr/lib64/R/library/zoo/NEWS
/usr/lib64/R/library/zoo/R/zoo
/usr/lib64/R/library/zoo/R/zoo.rdb
/usr/lib64/R/library/zoo/R/zoo.rdx
/usr/lib64/R/library/zoo/THANKS
/usr/lib64/R/library/zoo/TODO
/usr/lib64/R/library/zoo/WISHLIST
/usr/lib64/R/library/zoo/demo/zoo-overplot.R
/usr/lib64/R/library/zoo/doc/MSFT.rda
/usr/lib64/R/library/zoo/doc/demo1.txt
/usr/lib64/R/library/zoo/doc/demo2.txt
/usr/lib64/R/library/zoo/doc/index.html
/usr/lib64/R/library/zoo/doc/sunw.rda
/usr/lib64/R/library/zoo/doc/zoo-design.R
/usr/lib64/R/library/zoo/doc/zoo-design.Rnw
/usr/lib64/R/library/zoo/doc/zoo-design.pdf
/usr/lib64/R/library/zoo/doc/zoo-faq.R
/usr/lib64/R/library/zoo/doc/zoo-faq.Rnw
/usr/lib64/R/library/zoo/doc/zoo-faq.pdf
/usr/lib64/R/library/zoo/doc/zoo-quickref.R
/usr/lib64/R/library/zoo/doc/zoo-quickref.Rnw
/usr/lib64/R/library/zoo/doc/zoo-quickref.pdf
/usr/lib64/R/library/zoo/doc/zoo-read.R
/usr/lib64/R/library/zoo/doc/zoo-read.Rnw
/usr/lib64/R/library/zoo/doc/zoo-read.pdf
/usr/lib64/R/library/zoo/doc/zoo.R
/usr/lib64/R/library/zoo/doc/zoo.Rnw
/usr/lib64/R/library/zoo/doc/zoo.pdf
/usr/lib64/R/library/zoo/help/AnIndex
/usr/lib64/R/library/zoo/help/aliases.rds
/usr/lib64/R/library/zoo/help/paths.rds
/usr/lib64/R/library/zoo/help/zoo.rdb
/usr/lib64/R/library/zoo/help/zoo.rdx
/usr/lib64/R/library/zoo/html/00Index.html
/usr/lib64/R/library/zoo/html/R.css
/usr/lib64/R/library/zoo/include/zoo.h
/usr/lib64/R/library/zoo/tests/Examples/zoo-Ex.Rout.save
/usr/lib64/R/library/zoo/tests/as.Date.R
/usr/lib64/R/library/zoo/tests/as.Date.Rout.save
/usr/lib64/R/library/zoo/tests/bugfixes.R
/usr/lib64/R/library/zoo/tests/bugfixes.Rout.save
/usr/lib64/R/library/zoo/tests/na.fill.R
/usr/lib64/R/library/zoo/tests/na.fill.Rout.save
/usr/lib64/R/library/zoo/tests/na.locf.R
/usr/lib64/R/library/zoo/tests/na.locf.Rout.save
/usr/lib64/R/library/zoo/tests/vignette-zoo-quickref.R
/usr/lib64/R/library/zoo/tests/vignette-zoo-quickref.Rout.save
/usr/lib64/R/library/zoo/tests/vignette-zoo.R
/usr/lib64/R/library/zoo/tests/vignette-zoo.Rout.save

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/zoo/libs/zoo.so
/usr/lib64/R/library/zoo/libs/zoo.so.avx2
/usr/lib64/R/library/zoo/libs/zoo.so.avx512
