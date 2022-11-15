Name:		texlive-blochsphere
Version:	38388
Release:	1
Summary:	Draw pseudo-3D diagrams of Bloch spheres
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/blochsphere
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/blochsphere.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/blochsphere.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/blochsphere.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is used to draw pseudo-3D Blochsphere diagrams. It
supports various annotations, such as great and small circles,
axes, rotation markings and state vectors. It can be used in a
standalone fashion, or nested within a tikzpicture environment
by setting the environment option nested to true.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/blochsphere
%{_texmfdistdir}/tex/latex/blochsphere
%doc %{_texmfdistdir}/doc/latex/blochsphere

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
