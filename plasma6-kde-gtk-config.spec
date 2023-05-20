%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define git 20230520

Summary:	GTK2 and GTK3 configurator for KDE
Name:		plasma6-kde-gtk-config
Version:	5.240.0
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		System/Libraries
Url:		http://kde.org/
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/kde-gtk-config/-/archive/master/kde-gtk-config-master.tar.bz2#/kde-gtk-config-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/%{name}-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KDecoration2) >= 5.27.80
BuildRequires:	pkgconfig(atk)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	pkgconfig(pango)
BuildRequires:	gsettings-desktop-schemas
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	xsettingsd
BuildRequires:	sassc
Requires:	kde-cli-tools
Requires:	xsettingsd

%description
Configuration dialog to adapt GTK applications appearance to your taste
under KDE. Among its many features, it lets you:
- Choose which theme is used for GTK2 and GTK3 applications.
- Tweak some GTK applications behaviour.
- Select what icon theme to use in GTK applications.
- Select GTK applications default fonts.
- Easily browse and install new GTK2 and GTK3 themes.

%files
%{_libdir}/libexec/*
%{_libdir}/kconf_update_bin/gtk_theme
%{_qtdir}/plugins/kf6/kded/gtkconfig.so
%{_datadir}/kconf_update/gtkconfig.upd
%{_libdir}/gtk-3.0/modules/libcolorreload-gtk-module.so
%{_libdir}/gtk-3.0/modules/libwindow-decorations-gtk-module.so
%{_datadir}/themes/Breeze/window_decorations.css
%{_datadir}/kconf_update/remove_window_decorations_from_gtk_css.sh
%{_datadir}/kcm-gtk-module/preview.ui
%{_libdir}/kconf_update_bin/remove_deprecated_gtk4_option

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n kde-gtk-config-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
