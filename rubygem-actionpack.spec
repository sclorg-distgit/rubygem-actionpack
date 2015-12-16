%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from actionpack-1.13.5.gem by gem2rpm -*- rpm-spec -*-
%global gem_name actionpack


Summary: Web-flow and rendering framework putting the VC in MVC
Name: %{?scl_prefix}rubygem-%{gem_name}
Epoch: 1
Version: 4.0.2
Release: 4%{?dist}
Group: Development/Languages
License: MIT
URL: http://www.rubyonrails.org
Source0: http://rubygems.org/downloads/actionpack-%{version}.gem

# Also the actionpack gem doesn't ship with the test suite.
# You may check it out like so
# git clone http://github.com/rails/rails.git
# cd rails/actionpack/
# git checkout v4.0.2
# tar czvf actionpack-4.0.2-tests.tgz test/
Source2: actionpack-%{version}-tests.tgz
Patch0: rubygem-actionpack-enable-test.patch
# Fix for CVE-2014-0081:
# number_to_currency, number_to_percentage and number_to_human XSS vulnerability
Patch1: rubygem-actionpack-4.0.3-CVE-2014-0081-XSS-vulnerability.patch
# Fix for CVE-2014-0130
Patch2: rubygem-actionpack-4.0.5-CVE-2014-0130-avoid-dir-traversal.patch

# Let's keep Requires and BuildRequires sorted alphabeticaly
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(activemodel) = %{version}
Requires: %{?scl_prefix}rubygem(activesupport) = %{version}
Requires: %{?scl_prefix}rubygem(builder) >= 3.1.0
Requires: %{?scl_prefix}rubygem(builder) < 3.2
Requires: %{?scl_prefix}rubygem(erubis) >= 2.7.0
Requires: %{?scl_prefix}rubygem(erubis) < 2.8
#Requires: %{?scl_prefix}rubygem(journey) >= 1.0.4
#Requires: %{?scl_prefix}rubygem(journey) < 1.1
Requires: %{?scl_prefix}rubygem(rack) >= 1.5.2
Requires: %{?scl_prefix}rubygem(rack) < 1.6
Requires: %{?scl_prefix}rubygem(rack-cache) >= 1.2
Requires: %{?scl_prefix}rubygem(rack-cache) < 2
Requires: %{?scl_prefix}rubygem(rack-test) >= 0.6.2
Requires: %{?scl_prefix}rubygem(rack-test) < 0.7
Requires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix}rubygem(activemodel) = %{version}
BuildRequires: %{?scl_prefix}rubygem(activerecord) = %{version}
BuildRequires: %{?scl_prefix}rubygem(activesupport) = %{version}
BuildRequires: %{?scl_prefix}rubygem(erubis) >= 2.7.0
BuildRequires: %{?scl_prefix}rubygem(erubis) < 2.8
#BuildRequires: %{?scl_prefix}rubygem(journey) >= 1.0.4
#BuildRequires: %{?scl_prefix}rubygem(journey) < 1.1
BuildRequires: %{?scl_prefix_ruby}rubygem(minitest)
BuildRequires: %{?scl_prefix}rubygem(mocha) >= 0.9.8
BuildRequires: %{?scl_prefix}rubygem(rack) >= 1.5.2
BuildRequires: %{?scl_prefix}rubygem(rack) < 1.6
BuildRequires: %{?scl_prefix}rubygem(rack-cache) >= 1.2
BuildRequires: %{?scl_prefix}rubygem(rack-cache) < 2
BuildRequires: %{?scl_prefix}rubygem(rack-test) >= 0.6.2
BuildRequires: %{?scl_prefix}rubygem(rack-test) < 0.7
BuildRequires: %{?scl_prefix}rubygem(sqlite3)
BuildRequires: %{?scl_prefix}rubygem(therubyracer)
%{?scl:BuildRequires: scldevel(v8)}
BuildRequires: %{?scl_prefix}rubygem(tzinfo) >= 0.3.29
BuildRequires: %{?scl_prefix}rubygem(tzinfo) < 0.4
BuildRequires: %{?scl_prefix}rubygem(uglifier)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Eases web-request routing, handling, and response as a half-way front,
half-way page controller. Implemented with specific emphasis on enabling easy
unit/integration testing that doesn't require a browser.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires:%{?scl_prefix}%{pkg_name} = %{epoch}:%{version}-%{release}

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - << \EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

# move the tests into place
tar xzvf %{SOURCE2} -C .%{gem_instdir}

pushd .%{gem_instdir}
%patch0 -p0
%patch1 -p1
%patch2 -p1
popd

# Remove backup files
# No! these are needed for rake test
# find ./%{gem_instdir} -type f -name "*~" -delete

# Delete zero-length files
# No! these are also needed for rake test
# find ./%{gem_instdir} -type f -size 0c -exec rm -rvf {} \;

# Fix anything executable that does not have a shebang
for file in `find ./%{gem_instdir} -type f -perm /a+x`; do
    [ -z "`head -n 1 $file | grep \"^#!/\"`" ] && chmod -v 644 $file
done

# Find files with a shebang that do not have executable permissions
for file in `find ./%{gem_instdir} -type f ! -perm /a+x -name "*.rb"`; do
    [ ! -z "`head -n 1 $file | grep \"^#!/\"`" ] && chmod -v 755 $file
done

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}

%clean
rm -rf %{buildroot}

%check
pushd .%{gem_instdir}

# load_path is not available, remove its require.
sed -i '1,2d' test/abstract_unit.rb

# dependency loop
# depends on actionmailer, while actionmailer has BR(check): actionpack
mv test/controller/assert_select_test.rb \
            test/controller/assert_select_test.rb.skip

# dependency loop
# depends on rails/engine from Railties
mv test/dispatch/routing/inspector_test.rb \
            test/dispatch/routing/inspector_test.rb.skip

# fix rack/test requirement
sed -i "1i\require 'rack/test'" lib/action_controller/metal/strong_parameters.rb

%{?scl:scl enable %{scl} - << \EOF}
ruby -w -I.:lib:test -e 'Dir.glob("test/{abstract,controller,dispatch,template}/**/*_test.rb").each {|t| require t}'
%{?scl:EOF}
# activerecord tests must be run separately, otherwise we get superclass mismatch error
# due to test classes that have same names in activerecord and other tests
%{?scl:scl enable %{scl} - << \EOF}
ruby -w -I.:lib:test -e 'Dir.glob("test/activerecord/**/*_test.rb").each {|t| require t}'
%{?scl:EOF}
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/test/

%changelog
* Wed May 07 2014 Josef Stribny <jstribny@redhat.com> - 1:4.0.2-4
- Fix for CVE-2014-0130
  - Resolves: rhbz#1095172

* Tue Feb 18 2014 Josef Stribny <jstribny@redhat.com> - 1:4.0.2-3
- Fixes for CVE-2014-0081
  - Resolves: rhbz#1065587

* Mon Feb 17 2014 Josef Stribny <jstribny@redhat.com> - 1:4.0.2-2
- Depend on scldevel(v8) virtual provide

* Wed Dec 04 2013 Josef Stribny <jstribny@redhat.com> - 1:4.0.2-1
- Update to ActionPack 4.0.2
  - Resolves: rhbz#1037985
- Fix CVE-2013-6417, CVE-2013-6414, CVE-2013-6415, CVE-2013-6416 and CVE-2013-4491
  - Resolves: rhbz#1036421

* Thu Nov 21 2013 Josef Stribny <jstribny@redhat.com> - 1:4.0.1-1
- Update to ActionPack 4.0.1

* Wed Oct 16 2013 Josef Stribny <jstribny@redhat.com> - 1:4.0.0-2
- Convert to scl

* Thu Aug 08 2013 Josef Stribny <jstribny@redhat.com> - 1:4.0.0-1
- Update to ActionPack 4.0.0.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.2.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 20 2013 Vít Ondruch <vondruch@redhat.com> - 1:3.2.13-2
- Test suite passes once again.

* Tue Mar 19 2013 Vít Ondruch <vondruch@redhat.com> - 1:3.2.13-1
- Update to the ActionPack 3.2.13.

* Fri Mar 08 2013 Vít Ondruch <vondruch@redhat.com> - 1:3.2.12-2
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Tue Feb 12 2013 Vít Ondruch <vondruch@redhat.com> - 1:3.2.12-1
- Update to the ActionPack 3.2.12.

* Wed Jan 09 2013 Vít Ondruch <vondruch@redhat.com> - 1:3.2.11-1
- Update to the ActionPack 3.2.11.

* Thu Jan 03 2013 Vít Ondruch <vondruch@redhat.com> - 1:3.2.10-1
- Update to the ActionPack 3.2.10.

* Sat Oct 13 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.2.8-2
- Relaxed Builder dependency.

* Mon Aug 13 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.2.8-1
- Update to the ActionPack 3.2.8.

* Wed Aug 01 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.2.7-2
- Remove the unneded symlink used for tests in previous versions (RHBZ #840119).

* Mon Jul 30 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.2.7-1
- Update to the ActionPack 3.2.7.

* Tue Jul 24 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.2.6-2
- Fixed missing epoch in -doc subpackage.

* Mon Jul 23 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.2.6-1
- Updated to the ActionPack 3.2.6.
- Remove Rake dependency.
- Introduce -doc subpackage.
- Relax sprockets dependency.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.0.15-1
- Updated to the ActionPack 3.0.15.

* Fri Jun 01 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.0.13-1
- Updated to the ActionPack 3.0.13.

* Fri Mar 16 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.0.11-3
- The CVE patches names now contain the CVE id.

* Tue Mar 06 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.0.11-2
- Fix for CVE-2012-1098.
- Fix for CVE-2012-1099.

* Tue Jan 31 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.0.11-1
- Rebuilt for Ruby 1.9.3.
- Updated to ActionPack 3.0.11.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 22 2011 Vít Ondruch <vondruch@redhat.com> - 1:3.0.10-1
- Update to ActionPack 3.0.10

* Mon Jul 04 2011 Vít Ondruch <vondruch@redhat.com> - 1:3.0.9-1
- Update to ActionPack 3.0.9

* Thu Jun 16 2011 Mo Morsi <mmorsi@redhat.com> - 1:3.0.5-3
- Include fix for CVE-2011-2197

* Fri Jun 03 2011 Vít Ondruch <vondruch@redhat.com> - 1:3.0.5-2
- Removed regin and multimap dependencies. They were added into rack-mount
  where they actually belongs.

* Fri Mar 25 2011 Vít Ondruch <vondruch@redhat.com> - 1:3.0.5-1
- Updated to ActionPack 3.0.5

* Wed Feb 16 2011 Vít Ondruch <vondruch@redhat.com> - 1:3.0.3-4
- Relaxed erubis dependency
- Fixed build compatibility with RubyGems 1.5

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 07 2011 Mohammed Morsi <mmorsi@redhat.com> - 1:3.0.3-2
- changelog fixes

* Mon Jan 10 2011 Mohammed Morsi <mmorsi@redhat.com> - 1:3.0.3-1
- Update to rails 3

* Thu Aug 12 2010 Mohammed Morsi <mmorsi@redhat.com> - 1:2.3.8-2
- Bumped actionpack rack dependency to version 1.1.0

* Mon Aug 09 2010 Mohammed Morsi <mmorsi@redhat.com> - 1:2.3.8-1
- Update to 2.3.8

* Mon May 17 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1:2.3.5-2
- Set TMPDIR environment at %%check to make it sure all files created
  during rpmbuild are cleaned up

* Thu Jan 28 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1:2.3.5-1
- Update to 2.3.5

* Fri Jan  8 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1:2.3.4-4
- Workaround patch to fix for rack 1.1.0 dependency (bug 552972)

* Thu Dec 10 2009 David Lutterkort <lutter@redhat.com> - 1:2.3.4-3
- Patch for CVE-2009-4214 (bz 542786)

* Wed Oct  7 2009 David Lutterkort <lutter@redhat.com> - 1:2.3.4-2
- Bump Epoch to ensure upgrade path from F-11

* Sun Sep 20 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.3.4-1
- Update to 2.3.4 (bug 520843, CVE-2009-3009)
- Fix tests

* Sun Aug  2 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.3.3-1
- 2.3.3
- Enable test (some tests fail, please someone investigate!!)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 16 2009 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 2.3.2-1
- New upstream version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 23 2008 David Lutterkort <lutter@redhat.com> - 2.2.2-1
- New version

* Tue Sep 16 2008 David Lutterkort <dlutter@redhat.com> - 2.1.1-1
- New version (fixes CVE-2008-4094)

* Thu Jul 31 2008 Michael Stahnke <stahnma@fedoraproject.org> - 2.1.0-1
- New Upstream

* Tue Apr  8 2008 David Lutterkort <dlutter@redhat.com> - 2.0.2-2
- Fix dependency

* Mon Apr 07 2008 David Lutterkort <dlutter@redhat.com> - 2.0.2-1
- New version

* Mon Dec 10 2007 David Lutterkort <dlutter@redhat.com> - 2.0.1-1
- New version

* Thu Nov 29 2007 David Lutterkort <dlutter@redhat.com> - 1.13.6-1
- New version

* Tue Nov 13 2007 David Lutterkort <dlutter@redhat.com> - 1.13.5-2
- Fix buildroot; mark docs in geminstdir cleanly

* Tue Oct 30 2007 David Lutterkort <dlutter@redhat.com> - 1.13.5-1
- Initial package
