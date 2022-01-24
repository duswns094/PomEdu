// Call the dataTables jQuery plugin
$(document).ready(function() {
  var table = $('#dataTable').DataTable({
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
    // 전체 체크 해제하는 부분
    $(".del-chk").on('click',function(e){
        if($('input[class=del-chk]:checked').length==$(".del-chk").length){
            $(".dt_all_chk").prop('checked',true);
        }else{
            $(".dt_all_chk").prop('checked',false);
    }
    });

  var studentTable = $('#studentTable').DataTable({
    dom: 'ftp',
    order: [[ 1, 'asc' ]],
    "language": {
        "emptyTable": "데이터가 없어요.",
        "lengthMenu": "페이지당 _MENU_ 개씩 보기",
        "info": "현재 _START_ - _END_ / _TOTAL_건",
        "infoEmpty": "데이터 없음",
        "infoFiltered": "( _MAX_건의 데이터에서 필터링됨 )",
        "search": "검색: ",
        "zeroRecords": "일치하는 데이터가 없어요.",
        "loadingRecords": "로딩중...",
        "processing":     "잠시만 기다려 주세요...",
        "paginate": {
            "next": "다음",
            "previous": "이전"
        }
    },
    pageLength: 5,
    "lengthChange": false,
  });
   // 전체 체크 하는 부분
    $(".st_all_chk").on( "click", function(e) {
        if($('.st_all_chk').is(':checked')){
            $('.st-del-chk').prop('checked',true);
        }else{
            $('.st-del-chk').prop('checked',false);
    }
    });
    // 전체 체크 해제하는 부분
    $(".st-del-chk").on('click',function(e){
        if($('input[class=st-del-chk]:checked').length==$(".st-del-chk").length){
            $(".st_all_chk").prop('checked',true);
        }else{
            $(".st_all_chk").prop('checked',false);
    }
    });

  var lectureTable = $('#lectureTable').DataTable({
    dom: 'ftp',
    order: [[ 1, 'asc' ]],
    "language": {
        "emptyTable": "데이터가 없어요.",
        "lengthMenu": "페이지당 _MENU_ 개씩 보기",
        "info": "현재 _START_ - _END_ / _TOTAL_건",
        "infoEmpty": "데이터 없음",
        "infoFiltered": "( _MAX_건의 데이터에서 필터링됨 )",
        "search": " 검색: ",
        "zeroRecords": "일치하는 데이터가 없어요.",
        "loadingRecords": "로딩중...",
        "processing":     "잠시만 기다려 주세요...",
        "paginate": {
            "next": "다음",
            "previous": "이전"
        }
    },
    pageLength: 5,
    "lengthChange": false,
  });
    // 전체 체크 하는 부분
    $(".lt_all_chk").on( "click", function(e) {
        if($('.lt_all_chk').is(':checked')){
            $('.lt-del-chk').prop('checked',true);
        }else{
            $('.lt-del-chk').prop('checked',false);
    }
    });
    // 전체 체크 해제하는 부분
    $(".lt-del-chk").on('click',function(e){
        if($('input[class=lt-del-chk]:checked').length==$(".lt-del-chk").length){
            $(".lt_all_chk").prop('checked',true);
        }else{
            $(".lt_all_chk").prop('checked',false);
    }
    });
    $('#create-item').on("click", function () {
        if(confirm("정말 등록하시겠습니까?")){
            var student_check = $("input[class=st-del-chk]:checked");
            var lecture_check = $("input[class=lt-del-chk]:checked");
            var student_id = [];
            var lecture_id = [];
            var csrf = $('input[name=csrfmiddlewaretoken').val();
            student_check.each(function(i){
                student_id[i]=$(this).val()
            })
            lecture_check.each(function(j){
                lecture_id[j]=$(this).val()
            })
            if(student_id.length==0){
                alert("학생을 선택해주세요")
            }else if(lecture_id.length==0){
                alert("강의를 선택해주세요")
            }else{
                console.log(student_id);
                console.log(lecture_id);
                $.ajax({
                    url:".",
                    method:"POST",
                    data:{
                        student_id,
                        lecture_id,
                        csrfmiddlewaretoken:csrf
                    },
                    success:function(response){
                        alert("성공");
                        location.href="../enrollment_list"
                        },
                    error:function(error){
                        alert("오류");
                        }
                    })
            }
        }
    });
});
function getCheckboxValue()  {
      // 선택된 목록 가져오기
      var student_name = [];
      var student_phoneNo = [];
      var student_check = $("input[class=st-del-chk]:checked");
      var lecture_check = $("input[class=lt-del-chk]:checked");
      student_check.each(function(i){
        var tr = student_check.parent().parent().eq(i);
        var td = tr.children();
        student_name[i]=td.eq(1).text();
        student_phoneNo[i]=td.eq(3).text();
      })
      var lecture_name = [];
      lecture_check.each(function(j){
        var tr = lecture_check.parent().parent().eq(j);
        var td = tr.children();
        lecture_name[j]=td.eq(1).text();
      })
      let result = '';
      for(var i=0;i<student_name.length;i++){
        for(var j=0;j<lecture_name.length;j++){
            result += '"'+student_name[i]+'"학생('+student_phoneNo[i]+')을 "'+lecture_name[j]+'"강의에 등록합니다.\n';
            }
        }
      document.getElementById('result').innerText = result;
    }
 // 게시글 삭제
function CheckItemDelete() {
        if(confirm("정말 삭제하시겠습니까?")){
            var id = [];
            $("input[class=del-chk]:checked").each(function(i){
                id[i]=$(this).val();
            })
            if(id.length==0){
                alert("삭제할 항목을 선택해주세요");
            }else{
               console.log(id);
               document.getElementById("frm").requestSubmit();
            }
        }
    };
function CheckItemDisable(){
        if(confirm("정말 비활성화 하시겠습니까?")){
            var id = [];
            $("input[class=del-chk]:checked").each(function(i){
                id[i]=$(this).val();
            })
            if(id.length==0){
                alert("비활성화할 항목을 선택해주세요");
            }else{
                console.log(id);
                a=$(this).value();
                document.getElementById("frm").submit();
            }
        }
    };

