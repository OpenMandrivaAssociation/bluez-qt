%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE Frameworks 5 Bluetooth module
Name:		bluez-qt
Version:	5.84.0
Release:	1
License:	LGPLv2.1+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org/
Source0:	http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5QuickTest)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Widgets)
# For building QCH docs
BuildRequires: qt5-assistant
BuildRequires:	doxygen
# For _udevrulesdir macro
BuildRequires:	systemd

%description
KDE Frameworks 5 Bluetooth module. It provides Qt wrapper for Bluez 5 DBus API.

%files
%{_udevrulesdir}/61-kde-bluetooth-rfkill.rules
%{_datadir}/qlogging-categories5/bluezqt.categories
%{_datadir}/qlogging-categories5/bluezqt.renamecategories

#----------------------------------------------------------------------------

%define qmlKF5BluezQt %mklibname KF5BluezQt-qml

%package -n %{qmlKF5BluezQt}
Summary:	QML plugin for KDE Frameworks 5 Bluetooth module
Group:		System/Libraries
Provides:	KF5BluezQt-qml = %{EVRD}

%description -n %{qmlKF5BluezQt}
QML plugin for KDE Frameworks 5 Bluetooth module.

%files -n %{qmlKF5BluezQt}
%dir %{_libdir}/qt5/qml/org/kde/bluezqt
%{_libdir}/qt5/qml/org/kde/bluezqt/libbluezqtextensionplugin.so
%{_libdir}/qt5/qml/org/kde/bluezqt/qmldir
%{_libdir}/qt5/qml/org/kde/bluezqt/DevicesModel.qml

#----------------------------------------------------------------------------

%define libKF5BluezQt_major 6
%define libKF5BluezQt %mklibname KF5BluezQt %{libKF5BluezQt_major}

%package -n %{libKF5BluezQt}
Summary:	KDE Frameworks 5 Bluetooth module shared library
Group:		System/Libraries
Requires:	%{name} = %{EVRD}
Requires:	%{qmlKF5BluezQt} = %{EVRD}
Obsoletes:	%{mklibname libKF5BluezQt 5}
Obsoletes:	%{mklibname libKF5BluezQt 6}

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
%{_libdir}/qt5/mkspecs/modules/qt_BluezQt.pri

#----------------------------------------------------------------------------
%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devKF5BluezQt} = %{EVRD}

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}
#----------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
