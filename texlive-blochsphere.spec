%global tl_name blochsphere
%global tl_revision 38388

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Draw pseudo-3D diagrams of Bloch spheres
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/blochsphere
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/blochsphere.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/blochsphere.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/blochsphere.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is used to draw pseudo-3D Blochsphere diagrams. It supports
various annotations, such as great and small circles, axes, rotation
markings and state vectors. It can be used in a standalone fashion, or
nested within a tikzpicture environment by setting the environment
option nested to true.

