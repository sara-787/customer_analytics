CONTAINER_NAME=customer_container

docker cp $CONTAINER_NAME:/app/pipeline/data_raw.csv ./results/
docker cp $CONTAINER_NAME:/app/pipeline/data_preprocessed.csv ./results/
docker cp $CONTAINER_NAME:/app/pipeline/insight1.txt ./results/
docker cp $CONTAINER_NAME:/app/pipeline/insight2.txt ./results/
docker cp $CONTAINER_NAME:/app/pipeline/insight3.txt ./results/
docker cp $CONTAINER_NAME:/app/pipeline/summary_plot.png ./results/
docker cp $CONTAINER_NAME:/app/pipeline/clusters.txt ./results/

docker stop $CONTAINER_NAME
docker rm $CONTAINER_NAME

echo "Results copied and container removed"