FROM metabase/metabase:latest

ENV JAVA_OPTS="-Xmx400m -Xms256m"
ENV MB_JETTY_HOST=0.0.0.0
ENV MB_JETTY_PORT=$PORT

CMD ["/app/run_metabase.sh"]