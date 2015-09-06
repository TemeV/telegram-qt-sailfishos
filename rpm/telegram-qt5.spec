Name:       telegram-qt5

# >> macros
# << macros
%define keepstatic 1

Summary:    Draft version of Telegram binding for Qt.
Version:    0.1.0
Release:    1
Group:      System/Libraries
License:    LGPL
URL:        http://example.org/
Source0:    %{name}-%{version}.tar.bz2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
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

# >> setup
# << setup

%build
# >> build pre
# << build pre

%cmake
make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/*.so.*
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_libdir}/cmake/TelegramQt5/TelegramQt5Config.cmake
%{_libdir}/cmake/TelegramQt5/TelegramQt5ConfigVersion.cmake
%{_includedir}/
# >> files devel
# << files devel
