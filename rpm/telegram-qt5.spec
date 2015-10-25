Name:       telegram-qt5

%define keepstatic 1

Summary:    Draft version of Telegram binding for Qt.
Version:    0.1.0
Release:    1
Group:      System/Libraries
License:    LGPL
URL:        http://example.org/
Source0:    %{name}-%{version}.tar.gz
Patch0:     fixcmake.patch
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  cmake
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  openssl-devel

%description
Draft version of Telegram binding for Qt.


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains libraries and header files for developing applications
that use %{name}.


%prep
%setup -q -n %{name}-%{version}/telegram-qt
# fixcmake.patch
%patch0 -p1

%build
%cmake
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_libdir}/cmake/TelegramQt5/TelegramQt5Config.cmake
%{_libdir}/cmake/TelegramQt5/TelegramQt5ConfigVersion.cmake
%{_includedir}/

