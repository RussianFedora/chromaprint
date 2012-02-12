Name:           chromaprint
Version:        0.6
Release:        4%{?dist}.R
Summary:        Library implementing the AcoustID fingerprinting

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://www.acoustid.org/chromaprint/
Source:         https://github.com/downloads/lalinsky/chromaprint/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  fftw-devel >= 3

%description
Chromaprint library is the core component of the AcoustID project. It's a 
client-side library that implements a custom algorithm for extracting 
fingerprints from raw audio sources.

The library exposes a simple C API. The documentation for the C API can be
found in the main header file.

%package -n libchromaprint
Summary:        Library implementing the AcoustID fingerprinting
Group:          System Environment/Libraries
Obsoletes:      python-chromaprint < 0.6-3

%description -n libchromaprint
Chromaprint library is the core component of the AcoustID project. It's a 
client-side library that implements a custom algorithm for extracting 
fingerprints from raw audio sources.

The library exposes a simple C API. The documentation for the C API can be
found in the main header file.

%package -n libchromaprint-devel
Summary:        Headers for developing programs that will use %{name} 
Group:          Development/Libraries
Requires:       libchromaprint%{?_isa} = %{version}-%{release}

%description -n libchromaprint-devel
This package contains the headers that programmers will need to develop
applications which will use %{name}. 


%prep
%setup -q

# examples require ffmpeg, so turn off examples
%{cmake} -DBUILD_EXAMPLES=off -DBUILD_TESTS=off


%build
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
rm  -f %{buildroot}%{_libdir}/lib*.la


%post -n libchromaprint -p /sbin/ldconfig

%postun -n libchromaprint -p /sbin/ldconfig

%files -n libchromaprint
%doc CHANGES.txt COPYING.txt NEWS.txt README.txt
%{_libdir}/lib*.so.*

%files -n libchromaprint-devel
%{_includedir}/chromaprint.h
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Tue Feb 7 2012 Ismael Olea <ismael@olea.org> - 0.6-4
- moved the obsoletes python-chromaprint to libchromaprint

* Mon Feb 6 2012 Ismael Olea <ismael@olea.org> - 0.6-3
- cosmetic SPEC changes
- obsoleting python-chromaprint (see #786946)

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 27 2011 Ismael Olea <ismael@olea.org> - 0.6-1
- update to 0.6
- python bindings removed
- python not a requirment now

* Wed Dec 07 2011 Ismael Olea <ismael@olea.org> - 0.5-4
- minor spec enhancements

* Mon Dec 05 2011 Ismael Olea <ismael@olea.org> - 0.5-3
- Macro cleaning at spec

* Thu Nov 18 2011 Ismael Olea <ismael@olea.org> - 0.5-2
- first version for Fedora

* Thu Nov 10 2011 Ismael Olea <ismael@olea.org> - 0.5-1
- update to 0.5
- subpackage for fpcalc 

* Sat Aug 06 2011 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.4-1
- Initial package
