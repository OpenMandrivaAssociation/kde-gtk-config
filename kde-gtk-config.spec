%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	GTK2 and GTK3 configurator for KDE
Name:		kde-gtk-config
Version:	5.14.2
Release:	1
License:	GPLv2+
Group:		System/Libraries
Url:		http://kde.org/
Source0:	http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz
Patch0:		kde-gtk-config-2.0-gtkrc-2.0-kde-config-file.patch
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	pkgconfig(atk)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	gsettings-desktop-schemas
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(pango)
Requires:	kde-cli-tools
Requires:	dconf
%rename	kde-gtk-config5

%description
Configuration dialog to adapt GTK applications appearance to your taste
under KDE. Among its many features, it lets you:
- Choose which theme is used for GTK2 and GTK3 applications.
- Tweak some GTK applications behaviour.
- Select what icon theme to use in GTK applications.
- Select GTK applications default fonts.
- Easily browse and install new GTK2 and GTK3 themes.

%files -f kde-gtk-config.lang
%{_sysconfdir}/xdg/*
%{_libdir}/libexec/*
%{_libdir}/qt5/plugins/kcm_*.so
%{_datadir}/icons/*/*/*/kde-gtk-config.*
%{_datadir}/kcm-gtk-module
%{_datadir}/kservices5/*.desktop

#----------------------------------------------------------------------------

%prep
%setup -q
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang kde-gtk-config || touch kde-gtk-config.lang
