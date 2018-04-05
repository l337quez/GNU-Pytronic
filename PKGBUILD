# Maintainer: "L337" Ronal Forero Leon (https://ronaldl337.wordpress.com/)


pkgname=gnu-pytronic
pkgver=0.001
pkgrel=1
pkgdesc="Slack Desktop (Beta) for Linux"
arch=('x86_64')
url="https://github.com/l337quez/GNU-Pytronic"
license=('GPL')
#depends=('alsa-lib' 'gconf' 'gtk2' 'libcurl-compat' 'libsecret' 'libxss' 'libxtst' 'nss')
#optdepends=('gnome-keyring')
#source=("https://downloads.slack-edge.com/linux_releases/${pkgname}-${pkgver}-amd64.deb"
#        "${pkgname}.patch")
#sha256sums=('03b72397311f555f598028bf5ef800f7449cc76544d9f9833798fc8dafeb1df9'
#            'c952eb32dd59beff9fc5374853b04acde4a60ed8c39934fcd0b66829455d594d')

#package() {
#    bsdtar -O -xf "slack-desktop-${pkgver}"*.deb data.tar.xz | bsdtar -C "${pkgdir}" -xJf -

    # Fix hardcoded icon path in .desktop file
#    patch -d "${pkgdir}" -p1 <"${pkgname}".patch

    # Permission fix
#    find "${pkgdir}" -type d -exec chmod 755 {} +

    # Remove all unnecessary stuff
#    rm -rf "${pkgdir}/etc"
#    rm -rf "${pkgdir}/usr/share/lintian"
#    rm -rf "${pkgdir}/usr/share/doc"

    # Move license
#    install -dm755 "${pkgdir}/usr/share/licenses/${pkgname}"
#    mv "${pkgdir}/usr/lib/slack/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}"
#    ln -s "/usr/share/licenses/${pkgname}/LICENSE" "${pkgdir}/usr/lib/slack/LICENSE"
#}
