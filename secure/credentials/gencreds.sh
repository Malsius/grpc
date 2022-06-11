printf "\e[0;31mRemoving old files\e[0m\n"
rm -rfv *.crt *.key *.csr *.srl

printf "\n\e[0;31mGenerating root key\e[0m\n"
openssl genrsa -out root.key 2048

printf "\n\e[0;31mGenerating server key\e[0m\n"
openssl genrsa -out server.key 2048

printf "\n\e[0;31mGenerating self signed root certificate\e[0m\n"
openssl req -new -x509 -days 365 -key root.key -out root.crt -subj "/C=FR/ST=Ile de France/L=Paris/O=Root/OU=IT/CN=localhost"
openssl x509 -in root.crt -noout -text

printf "\n\e[0;31mGenerating server certificate signing request\e[0m\n"
openssl req -new -key server.key -out server.csr -subj "/C=FR/ST=Ile de France/L=Paris/O=Server/OU=IT/CN=localhost"
openssl req -in server.csr -text -noout

printf "\n\e[0;31mGenerating server certificate signed with root CA\e[0m\n"
openssl x509 -req -in server.csr -out server.crt -CA root.crt -CAkey root.key -CAcreateserial
openssl x509 -in server.crt -noout -text

printf "\n\e[0;31mVerifying server certificate\e[0m\n"
openssl verify -CAfile root.crt server.crt