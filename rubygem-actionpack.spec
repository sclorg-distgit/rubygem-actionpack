%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from actionpack-1.13.5.gem by gem2rpm -*- rpm-spec -*-
%global gem_name actionpack

%global rubyabi 1.9.1

Summary: Web-flow and rendering framework putting the VC in MVC
Name: %{?scl_prefix}rubygem-%{gem_name}
Epoch: 1
Version: 3.2.8
Release: 20%{?dist}
Group: Development/Languages
License: MIT
URL: http://www.rubyonrails.org
Source0: http://rubygems.org/downloads/actionpack-%{version}.gem

# Also the actionpack gem doesn't ship with the test suite.
# You may check it out like so
# git clone http://github.com/rails/rails.git
# cd rails/actionpack/
# git checkout v3.2.8
# tar czvf actionpack-3.2.8-tests.tgz test/
Source2: actionpack-%{version}-tests.tgz

Patch0:  rubygem-actionpack-enable-test.patch
Patch1:  rubygem-actionpack-relax-sprockets-dependency.patch
Patch2:  rubygem-actionpack-3.2.11-CVE-2013-0156-xml_parsing.patch

# CVE-2013-0155
# https://bugzilla.redhat.com/show_bug.cgi?id=892866
Patch3:  rubygem-actionpack-3.2.11-CVE-2013-0155-null_array_param.patch

# CVE-2013-1855
# https://bugzilla.redhat.com/show_bug.cgi?id=921331
Patch4:  rubygem-actionpack-3.2.13-CVE-2013-1855-css_sanitize.patch

# CVE-2013-1857
# https://bugzilla.redhat.com/show_bug.cgi?id=921335
Patch5:  rubygem-actionpack-3.2.13-CVE-2013-1857-sanitize_protocol.patch

# Fix i18n missing translation XSS (CVE-2013-4491).
# https://bugzilla.redhat.com/show_bug.cgi?id=1036922
Patch6:  rubygem-actionpack-3.2.16-CVE-2013-4491-Stop-using-i18ns-built-in-HTML-error-handling.patch

# Fix Action View DoS (CVE-2013-6414).
# https://bugzilla.redhat.com/show_bug.cgi?id=1036483
Patch7:  rubygem-actionpack-3.2.16-CVE-2013-6414-Only-use-valid-mime-type-symbols-as-cache-keys.patch

# Fix number_to_currency XSS (CVE-2013-6415)
# https://bugzilla.redhat.com/show_bug.cgi?id=1036910
Patch8:  rubygem-actionpack-3.2.16-CVE-2013-6415-Escape-the-unit-value-provided-to-number_to_currency.patch

# Unsafe Query Generation Risk in Ruby on Rails (incomplete fix for
# CVE-2013-0155) (CVE-2013-6417).
# https://bugzilla.redhat.com/show_bug.cgi?id=1036409
Patch9:  rubygem-actionpack-3.2.16-CVE-2013-6417-Deep-Munge-the-parameters-for-GET-and-POST.patch

# Fix regression introduced by CVE-2013-6415.
# https://github.com/rails/rails/issues/13160
# https://github.com/makandra/rails/commit/9e625d64656556ac30172ce5bcc800da463dd777
Patch10: rubygem-actionpack-3.2.17-repair-a-test-broken-by-the-number_to_currency-XSS-fix.patch

# Fix for CVE-2014-0081
Patch11: rubygem-actionpack-3.2.17-CVE-2014-0081-XSS-vulnerability.patch

# Fix for CVE-2014-0082
Patch12: rubygem-actionpack-3.2.17-CVE-2014-0082-dos.patch

# Fix for CVE-2014-0130
Patch13: rubygem-actionpack-3.2.18-CVE-2014-0130-avoid-dir-traversal.patch

# Fix CVE-2015-7576 Timing attack vulnerability in basic authentication
# https://bugzilla.redhat.com/show_bug.cgi?id=1301933
Patch14: rubygem-actionpack-3.2.22.1-CVE-2015-7576-fix-timing-attack-vulnerability.patch

# Fix CVE-2016-0751 Possible Object Leak and Denial of Service attack
# https://bugzilla.redhat.com/show_bug.cgi?id=1301946
Patch15: rubygem-actionpack-3.2.22.1-CVE-2016-0751-fix-possible-object-leak-and-denial-of-service-attack.patch

# Fix CVE-2016-0752 Possible Information Leak Vulnerability
# https://bugzilla.redhat.com/show_bug.cgi?id=1301963
Patch16: rubygem-actionpack-3.2.22.1-CVE-2016-0752-fix-possible-information-leak-vulnerability.patch

# Fix CVE-2016-2097: Directory traversal and information leak in Action View
# https://bugzilla.redhat.com/show_bug.cgi?id=1310043
Patch17: rubygem-actionpack-3.2.22.2-render_data_leak_2.patch

# Fix CVE-2016-2098: Code injection vulnerability.
# https://bugzilla.redhat.com/show_bug.cgi?id=1310054
Patch18: rubygem-actionpack-3.2.22.2-secure_inline_with_params.patch

# Fix CVE-2016-6316: Fix unsafe query generation risk.
# https://bugzilla.redhat.com/show_bug.cgi?id=1365008
Patch19: rubygem-actionpack-3.2.22.4-CVE-2016-6316-attribute-xss.patch
Patch20: rubygem-actionpack-3.2.22.4-CVE-2016-6316-attribute-xss-tests.patch

# Let's keep Requires and BuildRequires sorted alphabeticaly
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(activemodel) = %{version}
Requires: %{?scl_prefix}rubygem(activesupport) = %{version}
Requires: %{?scl_prefix}rubygem(builder) >= 3.0.0
Requires: %{?scl_prefix}rubygem(builder) < 3.1
Requires: %{?scl_prefix}rubygem(erubis) >= 2.7.0
Requires: %{?scl_prefix}rubygem(erubis) < 2.8
Requires: %{?scl_prefix}rubygem(journey) >= 1.0.4
Requires: %{?scl_prefix}rubygem(journey) < 1.1
Requires: %{?scl_prefix}rubygem(rack) >= 1.4.0
Requires: %{?scl_prefix}rubygem(rack) < 1.5
Requires: %{?scl_prefix}rubygem(rack-cache) >= 1.2
Requires: %{?scl_prefix}rubygem(rack-cache) < 2
Requires: %{?scl_prefix}rubygem(rack-test) >= 0.6.1
Requires: %{?scl_prefix}rubygem(rack-test) < 0.7
Requires: %{?scl_prefix}rubygem(sprockets) >= 2.1.3
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygem(activemodel) = %{version}
BuildRequires: %{?scl_prefix}rubygem(activerecord) = %{version}
BuildRequires: %{?scl_prefix}rubygem(activesupport) = %{version}
BuildRequires: %{?scl_prefix}rubygem(erubis) >= 2.7.0
BuildRequires: %{?scl_prefix}rubygem(erubis) < 2.8
BuildRequires: %{?scl_prefix}rubygem(journey) >= 1.0.4
BuildRequires: %{?scl_prefix}rubygem(journey) < 1.1
BuildRequires: %{?scl_prefix}rubygem(json)
BuildRequires: %{?scl_prefix}rubygem(minitest)
BuildRequires: %{?scl_prefix}rubygem(mocha) >= 0.9.8
BuildRequires: %{?scl_prefix}rubygem(rack) >= 1.4.0
BuildRequires: %{?scl_prefix}rubygem(rack) < 1.5
BuildRequires: %{?scl_prefix}rubygem(rack-cache) >= 1.2
BuildRequires: %{?scl_prefix}rubygem(rack-cache) < 2
BuildRequires: %{?scl_prefix}rubygem(rack-test) >= 0.6.1
BuildRequires: %{?scl_prefix}rubygem(rack-test) < 0.7
BuildRequires: %{?scl_prefix}rubygem(sprockets) >= 2.1.3
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
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            -V \
            --force --no-rdoc %{SOURCE0}
%{?scl:"}

# move the tests into place
tar xzvf %{SOURCE2} -C .%{gem_instdir}

pushd .%{gem_instdir}
%patch0 -p0
%patch2 -p2
%patch3 -p2
%patch4 -p2
%patch5 -p2
%patch6 -p2
%patch7 -p2
%patch8 -p2
%patch9 -p2
%patch10 -p2
%patch11 -p1
%patch12 -p1
%patch13 -p2
%patch14 -p2
%patch15 -p2
%patch16 -p2
%patch17 -p2
%patch18 -p2
%patch19 -p2

# create missing symlink
pushd test/fixtures/layout_tests/layouts/
ln -sf ../../symlink_parent/ symlinked
popd

popd

pushd .%{gem_dir}
%patch1 -p0
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


%check
pushd .%{gem_instdir}

patch -p2 < %{PATCH20}

# load_path is not available, remove its require.
sed -i '1,2d' test/abstract_unit.rb

# dependency loop
# depends on actionmailer, while actionmailer has BR(check): actionpack
mv test/controller/assert_select_test.rb \
            test/controller/assert_select_test.rb.skip

%{?scl:scl enable %{scl} %{scl_v8} - << \EOF}
ruby -w -I.:lib:test -e 'Dir.glob("test/{abstract,controller,dispatch,template}/**/*_test.rb").each {|t| require t}'
# activerecord tests must be run separately, otherwise we get superclass mismatch error
# due to test classes that have same names in activerecord and other tests
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
* Tue Aug 23 2016 Pavel Valena <pvalena@redhat.com> - 1:3.2.8-20
- Fix for CVE-2016-6316 cross-site scripting flaw in Action View
  Resolves: rhbz#1365008

* Tue Mar 08 2016 Vít Ondruch <vondruch@redhat.com> - 1:3.2.8-16
- Update the CVE-2016-2097 to the latest upstream version.
  Related: CVE-2016-2097
- Update the CVE-2016-2098 patch to the latest upstream version.
  Related: CVE-2016-2098

* Wed Feb 24 2016 Vít Ondruch <vondruch@redhat.com> - 1:3.2.8-15
- Fix Directory traversal and information leak in Action View.
  Resolves: CVE-2016-2097
- Fix code injection vulnerability.
  Resolves: CVE-2016-2098

* Tue Feb 23 2016 Vít Ondruch <vondruch@redhat.com> - 1:3.2.8-14
- Fix Timing attack vulnerability in Action Controller.
  Resolves: CVE-2015-7576
- Fix Possible Object Leak and Denial of Service attack.
  Resolves: CVE-2016-0751
- Fix Possible Information Leak Vulnerability.
  Resolves: CVE-2016-0752

* Wed May 14 2014 Vít Ondruch <vondruch@redhat.com> - 1:3.2.8-13
- Fixes for CVE-2014-0130
  - Resolves: rhbz#1096086

* Thu Feb 20 2014 Josef Stribny <jstribny@redhat.com> - 1:3.2.8-11
- Fix for  CVE-2014-0082
  - Resolves: rhbz#1065891

* Tue Feb 18 2014 Josef Stribny <jstribny@redhat.com> - 1:3.2.8-10
- Fix for CVE-2014-0081
  - Resolves: rhbz#1065891

* Mon Feb 17 2014 Josef Stribny <jstribny@redhat.com> - 1:3.2.8-9
- Depend on scldevel(v8) virtual provide
  - Resolves: rhbz#1065887

* Tue Feb 11 2014 Vít Ondruch <vondruch@redhat.com> - 1:3.2.8-8
- Fix regression introduced by CVE-2013-6415.
  - Resolves: rhbz#1038194

* Tue Dec 03 2013 Vít Ondruch <vondruch@redhat.com> - 1:3.2.8-7
- Fix i18n missing translation XSS.
  * rubygem-actionpack-3.2.16-CVE-2013-4491-Stop-using-i18ns-built-in-HTML-error-handling.patch
  - Resolves: CVE-2013-4491
- Fix Action View DoS.
  * rubygem-actionpack-3.2.16-CVE-2013-6414-Only-use-valid-mime-type-symbols-as-cache-keys.patch
  - Resolves: CVE-2013-6414
- Fix number_to_currency XSS.
  * rubygem-actionpack-3.2.16-CVE-2013-6415-Escape-the-unit-value-provided-to-number_to_currency.patch
  - Resolves: CVE-2013-6415
- Fix unsafe query generation risk in Ruby on Rails (incomplete fix for
  CVE-2013-0155) (CVE-2013-6417).
  * rubygem-actionpack-3.2.16-CVE-2013-6417-Deep-Munge-the-parameters-for-GET-and-POST.patch
  - Resolves: CVE-2013-6417

* Thu Nov 28 2013 Vít Ondruch <vondruch@redhat.com> - 1:3.2.8-6
- Build against v8314 SCL.

* Mon Mar 18 2013 Vít Ondruch <vondruch@redhat.com> - 1:3.2.8-5
- Updated patch for CVE-2013-1857 by upstream.

* Fri Mar 15 2013 Vít Ondruch <vondruch@redhat.com> - 1:3.2.8-4
- Fix for CVE-2013-1855 and CVE-2013-1857.

* Mon Jan 14 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.2.8-3
- Fix for CVE-2013-0155.

* Thu Jan 10 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.2.8-2
- Fix for CVE-2013-0156.

* Tue Sep 18 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.2.8-1
- Updated to ActionPack 3.2.8.

* Fri Jul 27 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.2.6-4
- Fixed the require in the -doc subpackage.

* Thu Jul 26 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.2.6-3
- Import from Fedora again.
- Specfile cleanup

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

* Wed Nov 14 2007 David Lutterkort <dlutter@redhat.com> - 1.13.5-2
- Fix buildroot; mark docs in geminstdir cleanly

* Tue Oct 30 2007 David Lutterkort <dlutter@redhat.com> - 1.13.5-1
- Initial package
