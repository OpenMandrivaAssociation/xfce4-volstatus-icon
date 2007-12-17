Summary:	This applicaion help safely mount/eject media
Name:		xfce4-volstatus-icon
Version:	0.1.0
Release:	%mkrel 5
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-volstatus-icon
Source0:	http://goodies.xfce.org/releases/xfce4-volstatus-icon/%{name}-%{version}.tar.bz2
BuildRequires:	libxfcegui4-devel >= 4.4.1
BuildRequires:	libglib2-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	exo-devel
Obsoletes:	xfce-volstatus-icon

%description
This application help safely mount/eject media.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std 

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README ChangeLog AUTHORS
%{_bindir}/%{name}
