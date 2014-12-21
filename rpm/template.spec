Name:           ros-indigo-sr-ronex-examples
Version:        0.9.15
Release:        0%{?dist}
Summary:        ROS sr_ronex_examples package

Group:          Development/Libraries
License:        LGPLv3
URL:            http://www.shadowrobot.com/products/ronex
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-controller-interface
Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-realtime-tools
Requires:       ros-indigo-ros-ethercat-model
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rospy
Requires:       ros-indigo-sr-ronex-hardware-interface
Requires:       ros-indigo-sr-ronex-msgs
Requires:       ros-indigo-sr-ronex-utilities
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-std-srvs
Requires:       ros-indigo-xacro
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-controller-interface
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-realtime-tools
BuildRequires:  ros-indigo-ros-ethercat-model
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-sr-ronex-hardware-interface
BuildRequires:  ros-indigo-sr-ronex-msgs
BuildRequires:  ros-indigo-sr-ronex-utilities
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-std-srvs
BuildRequires:  ros-indigo-xacro

%description
Package containing examples for the RoNeX boards.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun Dec 21 2014 Shadow Robot's software team <software@shadowrobot.com> - 0.9.15-0
- Autogenerated by Bloom

