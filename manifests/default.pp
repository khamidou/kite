$packages = ["postfix"]

package { $packages:
    ensure => present,
}
