FROM python:3.6.4

WORKDIR /root/
COPY r.txt /root/
RUN pip install -r r.txt
RUN mkdir -p /root/log/
COPY ./ /root/

VOLUME /root/log/

RUN ls ./*



ENV EOS_MAINNET "https://proxy.eosnode.tools"
ENV SYMBOL "EOS"

ENV TRANSFER_TO ""
ENV TRANSFER_FROM ""
ENV TRANSFER_QUANTITY "1"
ENV TRANSFER_MEMO "1-96-omgomgwtfwtf-8BUE5Y"

ENV PRIVATEKEY ''

ENV TRANSFER 'transfer'
ENV CONTRACT 'eosio.token'


EXPOSE 9100
ENTRYPOINT ["/usr/local/bin/python", "wool.py"]
