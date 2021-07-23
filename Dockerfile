FROM alpine:3.14
MAINTAINER pasi@pashi.net
ADD search.py /
RUN apk add --update py3-requests py3-oauthlib py3-deprecated py3-pip && pip3 install atlassian-python-api
WORKDIR /app
CMD ["/search.py", "--tags", "python", "--verbose"]