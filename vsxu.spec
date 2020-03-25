# TODO: VSXU_TM? (vsx_tmi.h, libtm64 / libtm64c)
#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	VSXu Music Visualizer
Summary(pl.UTF-8):	VSXu - wizualizacja muzyki
Name:		vsxu
Version:	0.5.1
Release:	3
License:	GPL v3
Group:		Libraries
#Source0Download: https://github.com/vovoid/vsxu/releases
Source0:	https://github.com/vovoid/vsxu/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	b4c31f1b0e9def4fa4920341cda3708f
Patch0:		%{name}-glfw3.patch
Patch1:		%{name}-icons.patch
Patch2:		%{name}-desktop.patch
Patch3:		%{name}-system-ftgl.patch
URL:		http://www.vsxu.com/
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	cmake >= 2.8
BuildRequires:	ftgl-devel
BuildRequires:	glew-devel >= 1.6.0
BuildRequires:	glfw-devel >= 3
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libpng-devel >= 2:1.2.46
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libstdc++-devel
BuildRequires:	opencv-devel
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel
BuildRequires:	xorg-lib-libXrandr >= 1.3.0
Requires:	OpenGL >= 2.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VSXu (VSX Ultra) is an OpenGL-based (hardware-accelerated), modular
programming environment with its main purpose to visualize music and
create real time graphic effects.

%description -l pl.UTF-8
VSXu (VSX Ultra) to oparte na OpenGL-u (sprzętowo akcelerowane),
modularne środowisko programistyczne, którego głównym celem jest
wizualizacja muzyki i tworzenie efektów graficznych w czasie
rzeczywistym.

%package libs
Summary:	Shared VSXu engine libraries
Summary(pl.UTF-8):	Biblioteki współdzielone silnika VSXu
Group:		Libraries
Requires:	glew >= 1.6.0
Requires:	libpng >= 2:1.2.46

%description libs
VSXu (VSX Ultra) is an OpenGL-based (hardware-accelerated), modular
programming environment with its main purpose to visualize music and
create real time graphic effects.

This package contains shared libraries.

%description libs -l pl.UTF-8
VSXu (VSX Ultra) to oparte na OpenGL-u (sprzętowo akcelerowane),
modularne środowisko programistyczne, którego głównym celem jest
wizualizacja muzyki i tworzenie efektów graficznych w czasie
rzeczywistym.

Ten pakiet zawiera biblioteki współdzielone.

%package devel
Summary:	Header files for VSXu libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek VSXu
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glew-devel >= 1.6.0
Requires:	libpng-devel >= 2:1.2.46
Requires:	libstdc++-devel

%description devel
Header files for VSXu libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek VSXu.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
# COPYING contains copyright notes, not only GPL text
%doc AUTHORS CHANGELOG COPYING README.md
%attr(755,root,root) %{_bindir}/obj2vxm
%attr(755,root,root) %{_bindir}/vsxl
%attr(755,root,root) %{_bindir}/vsxu_artiste
%attr(755,root,root) %{_bindir}/vsxu_player
%attr(755,root,root) %{_bindir}/vsxu_profiler
%attr(755,root,root) %{_bindir}/vsxu_server
%attr(755,root,root) %{_bindir}/vsxz
%dir %{_libdir}/vsxu
%dir %{_libdir}/vsxu/plugins
%attr(755,root,root) %{_libdir}/vsxu/plugins/*.so
%{_datadir}/vsxu
%{_desktopdir}/vsxu-artiste.desktop
%{_desktopdir}/vsxu-artiste-fullscreen.desktop
%{_desktopdir}/vsxu-player.desktop
%{_desktopdir}/vsxu-player-fullscreen.desktop
%{_desktopdir}/vsxu-server.desktop
%{_desktopdir}/vsxu-server-fullscreen.desktop
%{_pixmapsdir}/vsxu.xpm
%{_iconsdir}/hicolor/*x*/apps/vsxu.png

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvsxu_engine.so
%attr(755,root,root) %{_libdir}/libvsxu_engine_audiovisual.so
%attr(755,root,root) %{_libdir}/libvsxu_engine_graphics.so
%attr(755,root,root) %{_libdir}/libvsx_widget.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/vsxu
%{_pkgconfigdir}/libvsxu.pc
