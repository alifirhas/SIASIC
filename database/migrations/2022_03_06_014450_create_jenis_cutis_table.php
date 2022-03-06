<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('jenis_cutis', function (Blueprint $table) {
            $table->id();
            $table->string('nama_cuti', 50);
            $table->string('persyaratan', 200);
            $table->integer('jatah');
            $table->string('nip_pejabat', 18);
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('jenis_cutis');
    }
};
