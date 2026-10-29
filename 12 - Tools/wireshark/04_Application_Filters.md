---
tags: [wireshark, http, dns, tls, application]
tool: wireshark
---
# Application-Layer Filters (HTTP, DNS, TLS)

## HTTP
```
http                                  # all HTTP
http.request                          # requests only
http.response                         # responses only
http.request.method == "GET"
http.request.method == "POST"         # form submits — creds, uploads
http.response.code == 404
http.response.code >= 400             # all errors
http.host contains "example.com"
http.request.uri contains "login"
http contains "password"              # cleartext creds in HTTP
http.user_agent contains "curl"
```

## DNS
```
dns                                   # all DNS
dns.flags.response == 0               # queries
dns.flags.response == 1               # responses
dns.qry.name contains "example"
dns.qry.type == 1                     # A records
dns.flags.rcode != 0                  # DNS errors (NXDOMAIN etc.)
```
**Threat hunting:** unusually long/random `dns.qry.name` can indicate DNS tunneling/exfiltration.

## TLS / HTTPS
```
tls                                   # all TLS
tls.handshake.type == 1               # Client Hello
tls.handshake.type == 2               # Server Hello
tls.handshake.extensions_server_name  # SNI — the domain, visible even when encrypted
tls.record.version
```
**Note:** payload is encrypted, but the SNI (requested hostname) and certificate are visible — great for seeing *where* a host connects without decrypting.

## Other cleartext protocols (credential hunting in labs)
```
ftp                 # ftp.request.command == "USER" / "PASS"
telnet
smtp
pop || imap
snmp
```
