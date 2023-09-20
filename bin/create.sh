TEMPLATE_DIR=templates
TMP_DIR=templates/tmp
mkdir -p ${TMP_DIR}

echo "请输入实体名: "
read entity

capitalized_entity="$(tr '[:lower:]' '[:upper:]' <<< ${entity:0:1})${entity:1}"

declare -A ofiles=( [CTRL]=${TEMPLATE_DIR}/demo_ctrl.py
                    [MANAGER]=${TEMPLATE_DIR}/demo_manager.py
                    [DAO]=${TEMPLATE_DIR}/demo_dao.py
                    [API]=${TEMPLATE_DIR}/api_demo.proto
                    [ENTITY]=${TEMPLATE_DIR}/demo.proto )
declare -A nfiles=( [N_CTRL]=${TMP_DIR}/ctrl.py
                    [N_MANAGER]=${TMP_DIR}/manager.py
                    [N_DAO]=${TMP_DIR}/dao.py
                    [N_API]=${TMP_DIR}/api.proto
                    [N_ENTITY]=${TMP_DIR}/entity.proto )
declare -A dfiles=( [D_CTRL]="src/ctrl/${entity}_ctrl.py"
                    [D_MANAGER]="src/manager/${entity}_manager.py"
                    [D_DAO]="src/dao/${entity}_dao.py"
                    [D_API]="src/proto/api/api_${entity}.proto"
                    [D_ENTITY]="src/proto/entities/${entity}.proto")

for key in "${!ofiles[@]}"; do
    cp ${ofiles[$key]} ${nfiles[N_$key]}
done

for key in ${!nfiles[@]}; do
    sed -i "s/demo/${entity}/g" ${nfiles[$key]}
    sed -i "s/Demo/${capitalized_entity}/g" ${nfiles[$key]}
done

for key in "${!ofiles[@]}"; do
    cp ${nfiles[N_$key]} ${dfiles[D_$key]}
    echo "rm ${dfiles[D_$key]}"
done

rm -rf $TMP_DIR
