%global packname  DAAG
%global rlibdir  %{_libdir}/R/library

%define debug_package %{nil}

Name:             R-%{packname}
Version:          1.16
Release:          2
Summary:          Data Analysis And Graphics data and functions
Group:            Sciences/Mathematics
License:          Unlimited
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/DAAG_1.16.tar.gz
Requires:         R-MASS R-rpart R-randomForest R-boot R-survival 
Requires:         R-lattice R-leaps R-oz R-lme4 R-quantreg 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-MASS R-rpart R-randomForest R-boot R-survival
BuildRequires:    R-lattice R-leaps R-oz R-lme4 R-quantreg 

%description
various data sets used in examples and exercises in the book Maindonald,
J.H. and Braun, W.J. (2003, 2007, 2010) "Data Analysis and Graphics Using

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/misc
%{rlibdir}/%{packname}/seedrates.txt


%changelog
* Sun Feb 19 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.12-1
+ Revision: 777463
- Import R-DAAG
- Import R-DAAG



