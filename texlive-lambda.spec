Name:		texlive-lambda
Version:	20111102
Release:	1
Summary:	TeXLive lambda package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lambda.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
TeXLive lambda package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/lambda/base/UT1cmr.fd
%{_texmfdistdir}/tex/lambda/base/UT1omlgc.fd
%{_texmfdistdir}/tex/lambda/base/elhyph16.tex
%{_texmfdistdir}/tex/lambda/base/french.bgd
%{_texmfdistdir}/tex/lambda/base/french.lay
%{_texmfdistdir}/tex/lambda/base/grcodes.tex
%{_texmfdistdir}/tex/lambda/base/greek.bgd
%{_texmfdistdir}/tex/lambda/base/greek.lay
%{_texmfdistdir}/tex/lambda/base/grmhyph.tex
%{_texmfdistdir}/tex/lambda/base/inuit.hpn
%{_texmfdistdir}/tex/lambda/base/lambda.tex
%{_texmfdistdir}/tex/lambda/base/lchcmr.fd
%{_texmfdistdir}/tex/lambda/base/lchenc.def
%{_texmfdistdir}/tex/lambda/base/litcmr.fd
%{_texmfdistdir}/tex/lambda/base/litenc.def
%{_texmfdistdir}/tex/lambda/base/ocherokee.sty
%{_texmfdistdir}/tex/lambda/base/odev.sty
%{_texmfdistdir}/tex/lambda/base/ojapan.sty
%{_texmfdistdir}/tex/lambda/base/omarab.cfg
%{_texmfdistdir}/tex/lambda/base/omega.sty
%{_texmfdistdir}/tex/lambda/base/omlgc.cfg
%{_texmfdistdir}/tex/lambda/base/ot1omarb.fd
%{_texmfdistdir}/tex/lambda/base/ot1omlgc.fd
%{_texmfdistdir}/tex/lambda/base/ot1uctt.fd
%{_texmfdistdir}/tex/lambda/base/usenglish.bgd
%{_texmfdistdir}/tex/lambda/base/usenglish.lay
%{_texmfdistdir}/tex/lambda/base/ut1enc.def
%{_texmfdistdir}/tex/lambda/config/lambda.ini
%{_texmfdistdir}/tex/lambda/config/language.dat

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}