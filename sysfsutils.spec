Name:           sysfsutils
URL:            http://sourceforge.net/projects/linux-diag/
License:        GPLv2
Group:          Development/Tools
Version:        2.1.0
Release:        6.1%{?dist}

Summary:        Utilities for interfacing with sysfs
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source0:        http://prdownloads.sourceforge.net/linux-diag/%{name}-%{version}.tar.gz
Patch0:         sysfsutils-2.0.0-redhatify.patch
Patch1:         sysfsutils-2.0.0-class-dup.patch
Patch2:         sysfsutils-2.1.0-get_link.patch

%description
This package's purpose is to provide a set of utilities for interfacing
with sysfs.

%package -n libsysfs
Summary: Shared library for interfacing with sysfs
Group: System Environment/Libraries
License: LGPLv2+

%description -n libsysfs
Library used in handling linux kernel sysfs mounts and their various files.

%package -n libsysfs-devel
Summary: Static library and headers for libsysfs
Group: Development/Libraries
License: LGPLv2+
Requires: libsysfs = %{version}-%{release}

%description -n libsysfs-devel
libsysfs-devel provides the header files and static libraries required
to build programs using the libsysfs API.

%prep
%setup -q
%patch0 -p1 -b .redhatify
%patch1 -p1
%patch2 -p1

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

rm -f $RPM_BUILD_ROOT%{_bindir}/dlist_test $RPM_BUILD_ROOT%{_bindir}/get_bus_devices_list $RPM_BUILD_ROOT%{_bindir}/get_class_dev $RPM_BUILD_ROOT%{_bindir}/get_classdev_parent $RPM_BUILD_ROOT%{_bindir}/get_device $RPM_BUILD_ROOT%{_bindir}/get_driver $RPM_BUILD_ROOT%{_bindir}/testlibsysfs $RPM_BUILD_ROOT%{_bindir}/write_attr
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%post -n libsysfs -p /sbin/ldconfig

%postun -n libsysfs -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/systool
%{_bindir}/get_module
%{_mandir}/man1/systool.1.gz
%doc COPYING AUTHORS README NEWS CREDITS ChangeLog docs/libsysfs.txt cmd/GPL

%files -n libsysfs
%defattr(-,root,root)
%{_libdir}/libsysfs.so.*
%doc COPYING AUTHORS README NEWS CREDITS ChangeLog docs/libsysfs.txt lib/LGPL

%files -n libsysfs-devel
%defattr(-,root,root)
%dir %{_includedir}/sysfs
%{_includedir}/sysfs/libsysfs.h
%{_includedir}/sysfs/dlist.h
%{_libdir}/libsysfs.a
%{_libdir}/libsysfs.so


%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.1.0-6.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue May 20 2008 Jarod Wilson <jwilson@redhat.com> - 2.1.0-4
- Fix up get_link on kernel 2.6.25+ (#447220)

* Mon Feb 25 2008 Jarod Wilson <jwilson@redhat.com> - 2.1.0-3
- Review cleanups from Todd Zullinger (#226447)

* Thu Feb 14 2008 Jarod Wilson <jwilson@redhat.com> - 2.1.0-2
- Bump and rebuild with gcc 4.3

* Mon Sep 29 2007 Jarod Wilson <jwilson@redhat.com> - 2.1.0-1
- Update to upstream release 2.1.0

* Mon Sep 11 2006 Neil Horman <nhorman@redhat.com> - 2.0.0-6
- Integrate patch for bz 205808

* Mon Jul 17 2006 Jesse Keating <jkeating@redhat.com> - 2.0.0-5
- rebuild

* Mon Jul 10 2006 Neil Horman  <nhorman@redhat.com> - 2.0.0-4
- Obsoleting old sysfsutil-devel package for upgrade path (bz 198054)

* Fri Jul  7 2006 Doug Ledford <dledford@redhat.com> - 2.0.0-3
- Split the library and devel files out to libsysfs and leave the utils
  in sysfsutils.  This is for multilib arch requirements.

* Thu May 25 2006 Neil Horman <nhorman@redhat.com> - 2.0.0-2
- Fixed devel rpm to own sysfs include dir
- Fixed a typo in changelog

* Wed May 24 2006 Neil Horman <nhorman@redhat.com> - 2.0.0-1
- Rebase to sysfsutils-2.0.0 for RHEL5

* Thu Apr 27 2006 Jeremy Katz <katzj@redhat.com> - 1.3.0-2
- move .so to devel subpackage

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.3.0-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.3.0-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Jul 08 2005 Bill Nottingham  <notting@redhat.com> 1.3.0-1
- update to 1.3.0

* Wed Mar 02 2005 AJ Lewis <alewis@redhat.com> 1.2.0-4
- Rebuild

* Wed Feb 09 2005 AJ Lewis <alewis@redhat.com> 1.2.0-3
- start using %%configure instead of calling configure directly

* Wed Feb 09 2005 AJ Lewis <alewis@redhat.com> 1.2.0-2
- rebuild

* Mon Oct 11 2004 AJ Lewis <alewis@redhat.com> 1.2.0-1
- Update to upstream version 1.2.0

* Wed Sep 22 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- added /sbin/ldconfig calls to post/postun

* Thu Sep 01 2004 AJ Lewis <alewis@redhat.com> 1.1.0-2
- Fix permissions on -devel files

* Fri Aug 13 2004 AJ Lewis <alewis@redhat.com> 1.1.0-1.1
- Rebuild

* Fri Aug 13 2004 AJ Lewis <alewis@redhat.com> 1.1.0-1
- Initial package for FC3
