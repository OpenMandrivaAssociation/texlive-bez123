# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/bez123
# catalog-date 2009-09-02 11:33:10 +0200
# catalog-license lppl1.3
# catalog-version 1.1b
Name:		texlive-bez123
Version:	1.1b
Release:	1
Summary:	Support for Bezier curves
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bez123
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bez123.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bez123.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bez123.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides additional facilities in a picture environment for
drawing linear, cubic, and rational quadratic Bezier curves
(standard LaTeX only offers non-rational quadratic splines).
Provides a package multiply that provides a command for
multiplication of a length without numerical overflow.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bez123/bez123.sty
%{_texmfdistdir}/tex/latex/bez123/multiply.sty
%doc %{_texmfdistdir}/doc/latex/bez123/README
%doc %{_texmfdistdir}/doc/latex/bez123/bez123.pdf
#- source
%doc %{_texmfdistdir}/source/latex/bez123/bez123.dtx
%doc %{_texmfdistdir}/source/latex/bez123/bez123.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
