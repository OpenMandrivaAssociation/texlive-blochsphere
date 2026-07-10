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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is used to draw pseudo-3D Blochsphere diagrams. It supports
various annotations, such as great and small circles, axes, rotation
markings and state vectors. It can be used in a standalone fashion, or
nested within a tikzpicture environment by setting the environment
option nested to true.

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
%dir %{_datadir}/texmf-dist/doc/latex/blochsphere
%dir %{_datadir}/texmf-dist/source/latex/blochsphere
%dir %{_datadir}/texmf-dist/tex/latex/blochsphere
%doc %{_datadir}/texmf-dist/doc/latex/blochsphere/LICENSE
%doc %{_datadir}/texmf-dist/doc/latex/blochsphere/README.md
%doc %{_datadir}/texmf-dist/doc/latex/blochsphere/blochsphere.pdf
%doc %{_datadir}/texmf-dist/doc/latex/blochsphere/example.pdf
%doc %{_datadir}/texmf-dist/doc/latex/blochsphere/example.tex
%doc %{_datadir}/texmf-dist/source/latex/blochsphere/blochsphere.dtx
%doc %{_datadir}/texmf-dist/source/latex/blochsphere/blochsphere.ins
%{_datadir}/texmf-dist/tex/latex/blochsphere/blochsphere.sty
