FROM metabase/metabase:latest

ENV MB_JETTY_PORT=$PORT
ENV MB_DB_FILE=/metabase-data/metabase.db

EXPOSE 3000

CMD ["java", "-jar", "/app/metabase.jar"]