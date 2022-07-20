+++
date = "2022-07-19"
draft = false
title = "Clearing browser DNS cache"
[taxonomies]
  category = 'today-i-learnt'
  tag = 'dns'
+++


I currently use [NextDNS](https://nextdns.io) as my personal DNS server and adblocker,
along with [DNSSwitcher](https://mattmcneeney.github.io/DNSSwitcher/) for Mac. With this
setup I can quickly switch between different DNS servers quickly and unblock certain
websites instead of going to nextdns and adding them to the allowlist.  The problem here
is that even after changing my DNS servers, browsers have their own internal DNS caches
which refreshes at its own pace and would still send me to the NextDNS block page.  Thus
i needed a way to quickly clear cache on the browser if that happens.

To clear cache on

- **Firefox** visit **about:networking#dns** on the address bar and click on *Clear DNS Cache*
- **Chrome** visit **chrome://net-internals/#dns** on the address bar and goto tab *DNS* click on *Clear host cache*


The DNS is not only cached on the browser, but by the OS and perhaps various other layers.

To clear cache on *MacOSX* run the following

```bash
sudo dscacheutil -flushcache && sudo killall -HUP mDNSResponder
```
