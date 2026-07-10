%global tl_name bez123
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1b
Release:	%{tl_revision}.1
Summary:	Support for Bezier curves
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bez123
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bez123.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bez123.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bez123.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides additional facilities in a picture environment for drawing
linear, cubic, and rational quadratic Bezier curves (standard LaTeX only
offers non-rational quadratic splines). Provides a package multiply that
provides a command for multiplication of a length without numerical
overflow.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/bez123
%dir %{_datadir}/texmf-dist/source/latex/bez123
%dir %{_datadir}/texmf-dist/tex/latex/bez123
%doc %{_datadir}/texmf-dist/doc/latex/bez123/README
%doc %{_datadir}/texmf-dist/doc/latex/bez123/bez123.pdf
%doc %{_datadir}/texmf-dist/source/latex/bez123/bez123.dtx
%doc %{_datadir}/texmf-dist/source/latex/bez123/bez123.ins
%{_datadir}/texmf-dist/tex/latex/bez123/bez123.sty
%{_datadir}/texmf-dist/tex/latex/bez123/multiply.sty
