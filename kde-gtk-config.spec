%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	GTK2 and GTK3 configurator for KDE
Name:		kde-gtk-config
Version:	5.19.5
Release:	1
License:	GPLv2+
Group:		System/Libraries
Url:		http://kde.org/
Source0:	http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/%{name}-%{version}.tar.xz
Patch0:		kde-gtk-config-2.0-gtkrc-2.0-kde-config-file.patch
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	pkgconfig(atk)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(pango)
BuildRequires:	gsettings-desktop-schemas
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	xsettingsd
Requires:	kde-cli-tools
Requires:	xsettingsd
%rename	kde-gtk-config5

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
%{_datadir}/kcm-gtk-module
%{_libdir}/kconf_update_bin/gtk_theme
%{_libdir}/qt5/plugins/kf5/kded/gtkconfig.so
%{_datadir}/kconf_update/gtkconfig.upd
%{_libdir}/gtk-3.0/modules/libcolorreload-gtk-module.so

#----------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
