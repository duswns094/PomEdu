// Call the dataTables jQuery plugin
$(document).ready(function() {
  var table = $('#dataTable').DataTable({
//    select: {
//            style:'multi',
//            },
//    columnDefs: [ {
//            orderable: false,
//            className: 'select-checkbox',
//            targets:   0
//        } ],
    order: [[ 1, 'asc' ]],
    "language": {
        "emptyTable": "데이터가 없어요.",
        "lengthMenu": "페이지당 _MENU_ 개씩 보기",
        "info": "현재 _START_ - _END_ / _TOTAL_건",
        "infoEmpty": "데이터 없음",
        "infoFiltered": "( _MAX_건의 데이터에서 필터링됨 )",
        "search": " 에서 검색: ",
        "zeroRecords": "일치하는 데이터가 없어요.",
        "loadingRecords": "로딩중...",
        "processing":     "잠시만 기다려 주세요...",
        "paginate": {
            "next": "다음",
            "previous": "이전"
        }
    }
  });


    $('#delete-lecture').on("click", function () {
        if(confirm("정말 삭제하시겠습니까?")){
            var id = [];
            var csrf = $('input[name=csrfmiddlewaretoken').val();
            $("input[class=del-chk]:checked").each(function(i){
                id[i]=$(this).val()
            })
            if(id.length==0){
                alert("삭제할 항목을 선택해주세요")
            }else{
                console.log(id)
                $.ajax({
                    url:".",
                    method:"POST",
                    data:{
                        id,
                        csrfmiddlewaretoken:csrf
                    },
                    success:function(response){
                        for(var i=0;i<id.length;i++){
                        $('tr#'+id[i]+'').css('backgroud-color','#ccc');
                        $('tr#'+id[i]+'').fadeOut('slow');
                        document.location.reload(true);
                        }
                    }
                    })
            }
        }
    } );
    $('#dataTable_filter').prepend('<select id="select" class="custom-select custom-select-sm form-control form-control-sm" style="width:120px"></select>');

    $('#dataTable > thead > tr').children().each(function (indexInArray, valueOfElement) {
        $('#select').append('<option>'+valueOfElement.innerHTML+'</option>');
    });
    $('.dataTables_filter input').unbind().bind('keyup', function () {
        var colIndex = document.querySelector('#select').selectedIndex;
        table.column(colIndex).search(this.value).draw();
    });
    // 전체 체크 하는 부분
    $(".dt_all_chk").on( "click", function(e) {
        if($('.dt_all_chk').is(':checked')){
            $('.del-chk').prop('checked',true);
        }else{
            $('.del-chk').prop('checked',false);
    }
    });
    $(".del-chk").on('click',function(e){
        if($('input[class=del-chk]:checked').length==$(".del-chk").length){
            $(".dt_all_chk").prop('checked',true);
        }else{
            $(".dt_all_chk").prop('checked',false);
    }
    });
});



