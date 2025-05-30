#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v24
# autospec commit: a88ffdc
#
Name     : R-zoo
Version  : 1.8.14
Release  : 92
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/zoo_1.8-14.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/zoo_1.8-14.tar.gz
Summary  : S3 Infrastructure for Regular and Irregular Time Series (Z's
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-zoo-lib = %{version}-%{release}
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
observations. It is particularly aimed at irregular time series
             of numeric vectors/matrices and factors. zoo's key design goals
             are independence of a particular index/date/time class and
             consistency with ts and base R by providing methods to extend
             standard generics.

%package dev
Summary: dev components for the R-zoo package.
Group: Development
Requires: R-zoo-lib = %{version}-%{release}
Provides: R-zoo-devel = %{version}-%{release}
Requires: R-zoo = %{version}-%{release}

%description dev
dev components for the R-zoo package.


%package lib
Summary: lib components for the R-zoo package.
Group: Libraries

%description lib
lib components for the R-zoo package.


%prep
%setup -q -n zoo
pushd ..
cp -a zoo buildavx2
popd
pushd ..
cp -a zoo buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1744288678

%install
export SOURCE_DATE_EPOCH=1744288678
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/zoo/doc/msft2004.rda
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

%files dev
%defattr(-,root,root,-)
/usr/lib64/R/library/zoo/include/zoo.h

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/zoo/libs/zoo.so
/V4/usr/lib64/R/library/zoo/libs/zoo.so
/usr/lib64/R/library/zoo/libs/zoo.so
