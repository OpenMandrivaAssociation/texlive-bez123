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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides additional facilities in a picture environment for drawing
linear, cubic, and rational quadratic Bezier curves (standard LaTeX only
offers non-rational quadratic splines). Provides a package multiply that
provides a command for multiplication of a length without numerical
overflow.

