%define devname %mklibname msgpack-cpp -d

Name: msgpack-cpp
Version:	6.1.0
Release:	2
Source0: https://github.com/msgpack/msgpack-c/archive/cpp-%{version}.tar.gz
Summary: MessagePack implementation for C++
URL: https://msgpack.org/
License: Apache 2.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: boost-devel
BuildArch: noarch

%description
MessagePack implementation for C++.

MessagePack is an efficient binary serialization format. It lets you exchange
data among multiple languages like JSON. But it's faster and smaller.
Small integers are encoded into a single byte, and typical short strings
require only one extra byte in addition to the strings themselves.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C

%description -n %{devname}
Development files (Headers etc.) for %{name}.

MessagePack implementation for C++.

MessagePack is an efficient binary serialization format. It lets you exchange
data among multiple languages like JSON. But it's faster and smaller.
Small integers are encoded into a single byte, and typical short strings
require only one extra byte in addition to the strings themselves.

%prep
%autosetup -p1 -n msgpack-c-cpp-%{version}
%cmake \
	-DMSGPACK_CXX20=ON \
	-DMSGPACK_BUILD_EXAMPLES=OFF \
	-DMSGPACK_ENABLE_CXX=ON \
	-DMSGPACK_ENABLE_STATIC=ON

%build
%make_build -C build

%install
%make_install -C build

%files -n %{devname}
%{_includedir}/msgpack.hpp
%{_includedir}/msgpack
%{_libdir}/cmake/msgpack-cxx
