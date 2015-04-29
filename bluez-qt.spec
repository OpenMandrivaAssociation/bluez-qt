Summary:	KDE Frameworks 5 Bluetooth module
Name:		bluez-qt
Version:	5.3.0
Release:	1
License:	LGPLv2.1+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org/
Source0:	ftp://ftp.kde.org/pub/kde/stable/plasma/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	extra-cmake-modules
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5QuickTest)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Widgets)

%description
KDE Frameworks 5 Bluetooth module. It provides Qt wrapper for Bluez 5 DBus API.

%files
%{_udevrulesdir}/61-kde-bluetooth-rfkill.rules

#----------------------------------------------------------------------------

%define qmlkf5bluezqt %mklibname kf5bluezqt-qml

%package -n %{qmlkf5bluezqt}
Summary:	QML plugin for KDE Frameworks 5 Bluetooth module
Group:		System/Libraries
Provides:	kf5bluezqt-qml = %{EVRD}

%description -n %{qmlkf5bluezqt}
QML plugin for KDE Frameworks 5 Bluetooth module.

%files -n %{qmlkf5bluezqt}
%dir %{_kde5_qmldir}/org/kde/bluezqt/
%{_kde5_qmldir}/org/kde/bluezqt/*

#----------------------------------------------------------------------------

%define kf5bluezqt_major 5
%define libkf5bluezqt %mklibname kf5bluezqt %{kf5bluezqt_major}

%package -n %{libkf5bluezqt}
Summary:	KDE Frameworks 5 Bluetooth module shared library
Group:		System/Libraries
Requires:	%{name}
Requires:	%{qmlkf5bluezqt}

%description -n %{libkf5bluezqt}
KDE Frameworks 5 Bluetooth module shared library.

%files -n %{libkf5bluezqt}
%{_kde5_libdir}/libKF5BluezQt.so.%{kf5bluezqt_major}
%{_kde5_libdir}/libKF5BluezQt.so.%{version}

#----------------------------------------------------------------------------

%define devkf5bluezqt %mklibname kf5bluezqt -d

%package -n %{devkf5bluezqt}
Summary:	Development files for KDE Frameworks 5 Bluetooth module
Group:		Development/KDE and Qt
Requires:	%{libkf5bluezqt} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Provides:	kf5bluezqt-devel = %{version}

%description -n %{devkf5bluezqt}
This package contains header files needed if you wish to build applications
based on %{name}.

%files -n %{devkf5bluezqt}
%{_kde5_includedir}/KF5/BluezQt
%{_kde5_includedir}/KF5/bluezqt_version.h
%{_kde5_libdir}/cmake/KF5BluezQt
%{_kde5_libdir}/libKF5BluezQt.so
%{_kde5_mkspecsdir}/*.pri

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde5
%make

%install
%makeinstall_std -C build

