+++
date = "2022-07-19"
draft = false
title = "Clearing browser DNS cache"
[taxonomies]
  category = 'today-i-learnt'
  tag = 'dns'
+++


I currently use [NextDNS](https://nextdns.io) as my personal DNS server and adblocker,
along with [DNSSwitcher](https://mattmcneeney.github.io/DNSSwitcher/) for Mac to switch between
different DNS servers quickly to unblock certain websites. Even after changing my DNS servers, browsers have their own internal DNS caches which refreshes at its own pace and still sends me to the NextDNS block page.

To clear cache on

- **Firefox** visit **about:networking#dns** on the address bar and click on *Clear DNS Cache*
- **Chrome** visit **chrome://net-internals/#dns** on the address bar and goto tab *DNS* click on *Clear host cache*


The DNS is not only cached on the browser, but by the OS and perhaps various other layers.

To clear cache on the *MacOSX* run the following

```bash
sudo dscacheutil -flushcache && sudo killall -HUP mDNSResponder
```
