Name:		texlive-bez123
Version:	15878
Release:	1
Summary:	Support for Bezier curves
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bez123
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bez123.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bez123.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bez123.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
