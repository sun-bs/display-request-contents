# About
This is Flask sample that response all request contents.

# How to use
## docker
`docker build . -t display-request-contents`

`docker run -p 50080:80 --rm display-request-contents`

try:

`http://localhost:50080/test-path?test-query-key=test-query-value`

## docker-compose
`docker-compose up`

try:

`http://localhost:50080/test-path?test-query-key=test-query-value`

`http://localhost:60080/test-path?test-query-key=test-query-value`
