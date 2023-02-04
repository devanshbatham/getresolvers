<h1 align="center">
    getresolvers
  <br>
</h1>

<h4 align="center">A simple utility to fetch freshly updated DNS resolvers</h4>


<p align="center">
  <a href="#install">🏗️ Install</a>
  <a href="#usage">⛏️ Usage</a>
  <a href="#credits">📝 Credits</a>
  <br>
</p>


# Install
```sh
git clone https://github.com/Sybil-Scan/getresolvers
cd getresolvers
pip install .
```

# Usage

```sh
(~) >>> getresolvers

            __                   __
  ___ ____ / /________ ___ ___  / /  _____ _______
 / _ `/ -_) __/ __/ -_|_-</ _ \/ / |/ / -_) __(_-<
 \_, /\__/\__/_/  \__/___/\___/_/|___/\__/_/ /___/
/___/

                 - by Sybil Scan Research <research@sybilscan.com>

🔍 Fetching resolvers

1.1.189.244
1.1.189.228
1.1.187.97
1.1.178.251
1.1.178.221
1.1.178.200
1.1.136.105
...........
...........
1.0.249.11
1.0.233.246
1.0.232.226
1.0.231.206
1.0.216.157
1.0.216.155

✅ Resolvers found : 250
```

# Credits

Under the hood, the utility uses [dnsvalidator](https://github.com/vortexau/dnsvalidator) for fetching IPv4 DNS servers by verifying them against baseline servers, and ensuring accurate responses. The used Github action worflow is inspired from [fresh-resolvers](https://github.com/BonJarber/fresh-resolvers). 