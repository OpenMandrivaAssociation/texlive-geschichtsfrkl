# revision 25886
# category Package
# catalog-ctan /macros/latex/contrib/biblatex-contrib/geschichtsfrkl
# catalog-date 2012-04-08 13:49:02 +0200
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-geschichtsfrkl
Version:	1.1
Release:	9
Summary:	BibLaTeX style for historians
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/geschichtsfrkl
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/geschichtsfrkl.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/geschichtsfrkl.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/geschichtsfrkl.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a BibLaTeX style, (mostly) meeting the
requirements of the History Faculty of the University of
Freiburg (Germany).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/geschichtsfrkl/geschichtsfrkl.bbx
%{_texmfdistdir}/tex/latex/geschichtsfrkl/geschichtsfrkl.cbx
%doc %{_texmfdistdir}/doc/latex/geschichtsfrkl/README
%doc %{_texmfdistdir}/doc/latex/geschichtsfrkl/geschichtsfrkl.pdf
#- source
%doc %{_texmfdistdir}/source/latex/geschichtsfrkl/geschichtsfrkl.dtx
%doc %{_texmfdistdir}/source/latex/geschichtsfrkl/geschichtsfrkl.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Fri Apr 13 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 790576
- Import texlive-geschichtsfrkl
- Import texlive-geschichtsfrkl

