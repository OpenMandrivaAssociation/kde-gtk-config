Summary:	GTK2 and GTK3 configurator for KDE
Name:		kde-gtk-config
Version:	2.2.1
Release:	4
License:	GPLv3
Group:		Graphical desktop/KDE
Url:		https://projects.kde.org/projects/playground/base/kde-gtk-config
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz
Patch1:		kde-gtk-config-2.2-gtkrc-2.0-kde-config-file.patch

BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	kdelibs4-devel

%description
Configuration dialog to adapt GTK applications appearance to your taste
under KDE. Among its many features, it lets you:
- Choose which theme is used for GTK2 and GTK3 applications.
- Tweak some GTK applications behaviour.
- Select what icon theme to use in GTK applications.
- Select GTK applications default fonts.
- Easily browse and install new GTK2 and GTK3 themes.

%prep
%setup -q
%patch1 -p1

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name}

%files -f %{name}.lang
%doc README COPYING ChangeLog
%{_kde_libdir}/kde4/libexec/gtk_preview
%{_kde_libdir}/kde4/libexec/gtk3_preview
%{_kde_libdir}/kde4/libexec/reload_gtk_apps
%{_kde_libdir}/kde4/kcm_cgc.so
%{_kde_appsdir}/kcm-gtk-module/preview.ui
%{_kde_configdir}/cgcgtk3.knsrc
%{_kde_configdir}/cgcicon.knsrc
%{_kde_configdir}/cgctheme.knsrc
%{_kde_iconsdir}/hicolor/48x48/apps/kde-gtk-config.png
%{_kde_services}/kde-gtk-config.desktop

