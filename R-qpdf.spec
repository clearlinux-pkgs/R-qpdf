#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-qpdf
Version  : 1.1
Release  : 6
URL      : https://cran.r-project.org/src/contrib/qpdf_1.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/qpdf_1.1.tar.gz
Summary  : Split, Combine and Compress PDF Files
Group    : Development/Tools
License  : Apache-2.0
Requires: R-qpdf-lib = %{version}-%{release}
Requires: R-assertthat
BuildRequires : R-Rcpp
BuildRequires : R-askpass
BuildRequires : R-assertthat
BuildRequires : R-curl
BuildRequires : buildreq-R
BuildRequires : libjpeg-turbo-dev
BuildRequires : pkgconfig(zlib)
BuildRequires : zlib-dev

%description
as split, combine, and compress. This package interfaces directly to the 'qpdf' 
    C++ API and does not require any command line utilities. Note that 'qpdf' does

%package lib
Summary: lib components for the R-qpdf package.
Group: Libraries

%description lib
lib components for the R-qpdf package.


%prep
%setup -q -c -n qpdf

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552783256

%install
export SOURCE_DATE_EPOCH=1552783256
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library qpdf
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library qpdf
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library qpdf
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  qpdf || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/qpdf/DESCRIPTION
/usr/lib64/R/library/qpdf/INDEX
/usr/lib64/R/library/qpdf/Meta/Rd.rds
/usr/lib64/R/library/qpdf/Meta/features.rds
/usr/lib64/R/library/qpdf/Meta/hsearch.rds
/usr/lib64/R/library/qpdf/Meta/links.rds
/usr/lib64/R/library/qpdf/Meta/nsInfo.rds
/usr/lib64/R/library/qpdf/Meta/package.rds
/usr/lib64/R/library/qpdf/NAMESPACE
/usr/lib64/R/library/qpdf/NEWS
/usr/lib64/R/library/qpdf/R/qpdf
/usr/lib64/R/library/qpdf/R/qpdf.rdb
/usr/lib64/R/library/qpdf/R/qpdf.rdx
/usr/lib64/R/library/qpdf/help/AnIndex
/usr/lib64/R/library/qpdf/help/aliases.rds
/usr/lib64/R/library/qpdf/help/paths.rds
/usr/lib64/R/library/qpdf/help/qpdf.rdb
/usr/lib64/R/library/qpdf/help/qpdf.rdx
/usr/lib64/R/library/qpdf/html/00Index.html
/usr/lib64/R/library/qpdf/html/R.css
/usr/lib64/R/library/qpdf/tests/testthat.R
/usr/lib64/R/library/qpdf/tests/testthat/pdf-example-password.original.pdf
/usr/lib64/R/library/qpdf/tests/testthat/test-password-callback.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/qpdf/libs/qpdf.so
/usr/lib64/R/library/qpdf/libs/qpdf.so.avx2
