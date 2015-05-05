Summary:	KDE Frameworks 5 Bluetooth module
Name:		bluez-qt
Version:	5.3.0
Release:	1
License:	LGPLv2.1+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org/
Source0:	ftp://ftp.kde.org/pub/kde/stable/plasma/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
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

%define qmlKF5BluezQt %mklibname KF5BluezQt-qml

%package -n %{qmlKF5BluezQt}
Summary:	QML plugin for KDE Frameworks 5 Bluetooth module
Group:		System/Libraries
Provides:	KF5BluezQt-qml = %{EVRD}

%description -n %{qmlKF5BluezQt}
QML plugin for KDE Frameworks 5 Bluetooth module.

%files -n %{qmlKF5BluezQt}

#----------------------------------------------------------------------------

%define libKF5BluezQt_major 5
%define libKF5BluezQt %mklibname libKF5BluezQt %{libKF5BluezQt_major}

%package -n %{libKF5BluezQt}
Summary:	KDE Frameworks 5 Bluetooth module shared library
Group:		System/Libraries
Requires:	%{name} = %{EVRD}
Requires:	%{qmlKF5BluezQt} = %{EVRD}

%description -n %{libKF5BluezQt}
KDE Frameworks 5 Bluetooth module shared library.

%files -n %{libKF5BluezQt}
%{_libdir}/libKF5BluezQt.so.%{libKF5BluezQt_major}
%{_libdir}/libKF5BluezQt.so.%{version}

#----------------------------------------------------------------------------

%define devKF5BluezQt %mklibname KF5BluezQt -d

%package -n %{devKF5BluezQt}
Summary:	Development files for KDE Frameworks 5 Bluetooth module
Group:		Development/KDE and Qt
Requires:	%{libKF5BluezQt} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devKF5BluezQt}
This package contains header files needed if you wish to build applications
based on %{name}.

%files -n %{devKF5BluezQt}
%{_includedir}/KF5/BluezQt
%{_includedir}/KF5/bluezqt_version.h
%{_libdir}/cmake/KF5BluezQt
%{_libdir}/libKF5BluezQt.so

#----------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

