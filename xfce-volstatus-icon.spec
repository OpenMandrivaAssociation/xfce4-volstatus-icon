%define oname xfce4-volstatus-icon

Summary:	This applicaion help safely mount/eject media
Name:		xfce-volstatus-icon
Version:	0.1.0
Release:	%mkrel 4
License:	GPL
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-volstatus-icon
Source0:	http://goodies.xfce.org/releases/xfce4-volstatus-icon/%{oname}-%{version}.tar.bz2
BuildRequires:	libxfcegui4-devel >= 4.4.1
BuildRequires:	libglib2-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	exo-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This application help safely mount/eject media.

%prep
%setup -qn %{oname}-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std 

%find_lang %{oname}

%clean
rm -rf %{buildroot}

%files -f %{oname}.lang
%defattr(-,root,root)
%doc README ChangeLog COPYING AUTHORS
%{_bindir}/%{oname}
