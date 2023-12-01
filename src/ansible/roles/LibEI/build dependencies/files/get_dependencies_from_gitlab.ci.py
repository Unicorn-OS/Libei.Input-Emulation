# Uses gitlab.ci file to generate dependencies:
# https://gitlab.freedesktop.org/libinput/libei/-/tree/main/.gitlab-ci?ref_type=heads


def test()
    pkg = "git diffutils gcc gcc-c++ pkgconf-pkg-config systemd-devel libxkbcommon-devel libxml2 doxygen python3-attrs python3-pytest python3-dbusmock python3-jinja2 python3-pip python3-pyyaml hugo libabigail"

    arr = pkg.split(' ')

    for i in arr:
        print(f"- {i}")