Summary:	X Color Management tools
Summary(pl.UTF-8):	Narzędzia X Color Management (do zarządzania kolorami w X)
Name:		icc_examin
Version:	0.55
Release:	1
License:	MIT
Group:		X11/Applications/Graphics
Source0:	http://downloads.sourceforge.net/oyranos/%{name}-%{version}.tar.bz2
# Source0-md5:	51ba3b849eb47793974cab6956750cf0
Patch0:		%{name}-configure.patch
Patch1:		%{name}-paths.patch
Patch2:		%{name}-pld.patch
URL:		http://www.oyranos.org/icc-examin
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	fltk-devel >= 1.1.4
BuildRequires:	fltk-gl-devel >= 1.1.4
BuildRequires:	fontconfig-devel
BuildRequires:	ftgl-devel >= 2.1.2
BuildRequires:	gettext-tools
BuildRequires:	lcms-devel >= 1.14
BuildRequires:	libXcm-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	oyranos-devel >= 0.9.5
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
Requires:	fltk >= 1.1.4
# DejaVuSans.ttf
Requires:	fonts-TTF-DejaVu
Requires:	ftgl >= 2.1.2
Requires:	lcms >= 1.14
Requires:	oyranos-libs >= 0.9.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ICC Examin (unix name: iccexamin) is a viewer for the internals of a
ICC profile, measurement data (CGATS), argylls gamut VRML
visualisations and video card gamma tables.

%description -l pl.UTF-8
ICC Examin (polecenie iccexamin) to przeglądarka wnętrzności profili
ICC, danych pomiarowych (CGATS), wizualizacji VRML gam argylla oraz
tablic gamma kart graficznych.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
export CC="%{__cc}"
export CXX="%{__cxx}"
export CFLAGS="%{rpmcflags}"
export CXXFLAGS="%{rpmcxxflags}"
export LDFLAGS="%{rpmldflags}"
# NOTE: not autoconf configure, but mostly compatible
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# system DejaVuSans.ttf is used instead
%{__rm} $RPM_BUILD_ROOT%{_fontsdir}/FreeSans.ttf

# fix location of themable icon
install -d $RPM_BUILD_ROOT%{_iconsdir}
mv $RPM_BUILD_ROOT%{_pixmapsdir}/hicolor $RPM_BUILD_ROOT%{_iconsdir}

%find_lang icc_examin

%clean
rm -rf $RPM_BUILD_ROOT

%files -f icc_examin.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/iccexamin
%{_desktopdir}/iccexamin.desktop
%{_pixmapsdir}/iccexamin.png
%{_iconsdir}/hicolor/scalable/iccexamin.svg
%{_mandir}/man1/iccexamin.1*
