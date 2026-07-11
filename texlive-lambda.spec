%global tl_name lambda
%global tl_revision 45756

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	LaTeX for Omega and Aleph
Group:		Publishing
URL:		https://www.ctan.org/pkg/lambda
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lambda.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
LaTeX for Omega and Aleph

